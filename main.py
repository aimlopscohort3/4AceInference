from fastapi import FastAPI, Request, Form, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#from app.init import tokenizer, model  # Import from init.py
#from app.model_inference import generate_response  # Import inference logic


app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Input request schema
class ModelInput(BaseModel):
    input_text: str


@app.get("/", response_class=HTMLResponse)
async def render_ui(request: Request, response: str = None):
    """
    Renders the UI template.
    """
    return templates.TemplateResponse("index.html", {"request": request, "response": response})


@app.post("/predict/", response_class=HTMLResponse)
async def predict(request: Request, input_text: str = Form(...)):
    """
    Handles input text from the UI, generates a response using the model, 
    and renders the result back in the UI.
    """
    try:
        # Use the model_inference logic
        #generated_text = generate_response(input_text)
        generated_text ="Model generated text"

        # Render the response back in the UI
        return templates.TemplateResponse("index.html", {"request": request, "response": generated_text})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "response": f"Error: {str(e)}"})


#testing the model

# Endpoint for model inference
# @app.post("/generate")
# def generate_text(data: ModelInput):
#     try:
#         # Process input
#         input_text = data.input_text
#         inputs = tokenizer(input_text, return_tensors="pt")

#         # Generate output
#         outputs = model.generate(inputs["input_ids"], max_length=50, pad_token_id=tokenizer.pad_token_id)

#         # Decode response
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)

#         return {"input_text": input_text, "generated_text": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))