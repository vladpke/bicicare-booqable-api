from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/payment-completed")
async def payment_completed(id: str = Form(...), amount: str = Form(None)):
    print("🎉 Payment completed webhook received")
    print(f"ID: {id}")
    print(f"Amount: {amount}")
    return {"status": "received", "id": id, "amount": amount}
