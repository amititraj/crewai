import gradio as gr
import base64
from PIL import Image
from imageanalyzer.src.imageanalyzer.crew import Imageanalyzer

def main():

    css = """
        .title {
            font-size: 1em !important; 
            text-align: center !important;
            color: #FFD700; 
        }

        .subtitle {
            font-size: 0.5em !important; 
            text-align: center !important;
            color: #FFD700; 
        }

        .text {
            text-align: center;
        }
        """

    js = """
        function createGradioAnimation() {
            var container = document.createElement('div');
            container.id = 'gradio-animation';
            container.style.fontSize = '2em';
            container.style.fontWeight = 'bold';
            container.style.textAlign = 'center';
            container.style.marginBottom = '20px';
            container.style.color = '#eba93f';

            var text = 'Welcome to Image Analyzer';
            for (var i = 0; i < text.length; i++) {
                (function(i){
                    setTimeout(function(){
                        var letter = document.createElement('span');
                        letter.style.opacity = '0';
                        letter.style.transition = 'opacity 0.1s';
                        letter.innerText = text[i];

                        container.appendChild(letter);

                        setTimeout(function() {
                            letter.style.opacity = '0.9';
                        }, 50);
                    }, i * 250);
                })(i);
            }

            var gradioContainer = document.querySelector('.gradio-container');
            gradioContainer.insertBefore(container, gradioContainer.firstChild);

            return 'Animation created';
        }
        """    

    with gr.Blocks(theme=gr.themes.Ocean(), title="Image Analyzer", css=css, js=js) as demo:        

        with gr.Row():
            with gr.Column():
                file_input = gr.File(label="Upload Image File", file_types=["image"], height=125, scale=1,file_count="single")
                image_output = gr.Image(type="pil", label="Uploaded Image", height=300)

                def display_uploaded_file(file_obj):
                    try:
                        image = Image.open(file_obj.name)
                        return image
                    except Exception as e:
                        print(f"Error loading image: {e}")
                        return None

                file_input.change(fn=display_uploaded_file, inputs=file_input, outputs=image_output)

            with gr.Column():
                output_result = gr.Textbox(label="Image analysis", max_lines=20,interactive=False, lines=20)
        
        
        with gr.Row():
            with gr.Column():
                submit_btn = gr.Button("Submit 🚀")       

                def process_image(file_input):                                       

                    try:
                        image_path = file_input.name                        
                        inputs = {
                            'image_path': image_path
                        }
                        output_result = Imageanalyzer().crew().kickoff(inputs=inputs)
                        return output_result
                    except Exception as e:
                        raise Exception(f"An error occurred while running the crew: {e}")
                    

                submit_btn.click(fn=process_image, inputs=[file_input], 
                                 outputs=[output_result])
        
    demo.launch()

if __name__ == "__main__":
    main()        