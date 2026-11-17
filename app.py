from flask import Flask

@app.route('/')
def home():
    return "Welcome to the E-commerce Flask App!"