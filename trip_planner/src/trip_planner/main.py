#!/usr/bin/env python
import sys
import warnings
import gradio as gr
import json
from datetime import datetime
try:
    from .crew import TripPlanner
except Exception:
    # fall back to absolute import when running as a script
    from trip_planner.crew import TripPlanner

# from src.trip_planner import Itinerary

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def calculate_days(start_date, end_date):
    if not start_date or not end_date:
        return 0
    if start_date > end_date:
        return "End date should be after Start date"
    try:
        start = datetime.fromtimestamp(start_date)        
        end = datetime.fromtimestamp(end_date)
        delta = (end - start).days + 1
        return int(delta)
    except Exception as e:
        return f"Error: {str(e)}"

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

            var text = 'Welcome to Trip planner';
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
    
    budget_levels = ["Economy", "Standard", "Moderate", "Premium", "Luxury"]

    interest_level = [
    "Food & Drink",
    "Culture & History",
    "Shopping",
    "Nightlife",
    "Nature",
    "Adventure",
    "Sports"
]

    with gr.Blocks(theme=gr.themes.Ocean(), title="Trip planner using CrewAI", css=css, js=js) as demo:
        gr.Markdown("Trip planner using CrewAI", elem_classes="subtitle")

        with gr.Row():
            with gr.Column():
                destination = gr.Textbox(label="Enter your dream destination:") 
        
        # with gr.Row():
        #     with gr.Column():
        #         start_date = gr.DateTime(label="Select trip start date:",include_time=False) 

        with gr.Row():
            #with gr.Column():
            start_date = gr.DateTime(label="Select trip start date:",include_time=False) 
            end_date = gr.DateTime(label="Select trip end date:",include_time=False) 
            total_days = gr.Textbox(label="Total Days:",interactive=False)
            end_date.change(
                fn=calculate_days,
                inputs=[start_date, end_date],
                outputs=total_days
            )

        # with gr.Row():
        #     with gr.Column():
        #         total_days = gr.Textbox(label="Total Days:",interactive=False)

        with gr.Row():
            with gr.Column():
                budget = gr.Dropdown(choices=budget_levels, label="Select your travel budget",max_choices=1,multiselect=True)
                

        with gr.Row():
            with gr.Column():
                interests = gr.Dropdown(choices=interest_level, label="Select your travel interesets", multiselect=True)

        with gr.Row():
            with gr.Column():
                result = gr.Textbox(label="Trip plan & itinerary:",interactive=False, lines=15, visible=False)

        with gr.Row():
            with gr.Column():
                submit_btn = gr.Button("Submit 🚀")

                def process_trip(destination, start_date, end_date,total_days,budget,interests):                    
                    start = datetime.fromtimestamp(start_date).strftime("%Y-%m-%d")      
                    end = datetime.fromtimestamp(end_date).strftime("%Y-%m-%d")
                    #print(f"values:{destination}, {start}, {end},{total_days},{budget},{interests}")

                    inputs = {
                        "destination": destination,
                        "start_date": start,
                        "end_date": end,
                        "total_days": total_days,
                        "interests": interests,
                        "budget": budget,
                    }

                    print(f"input:{inputs}")

                    try:
                        result = TripPlanner().crew().kickoff(inputs=inputs)
                        return json.dumps(result.to_dict(), indent=2)
                        #print(f"search result:{result}")
                    except Exception as e:
                        raise Exception(f"An error occurred while running the crew: {e}")

                submit_btn.click(fn=process_trip, inputs=[destination, start_date, end_date,total_days,budget,interests], 
                                 outputs=[result]).then(
                                        fn=lambda x: gr.update(visible=True),
                                        inputs=result,
                                        outputs=result
                                    )
        
    demo.launch()

if __name__ == "__main__":
    main()

        