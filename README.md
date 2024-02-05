# AWS: Lambda-Function, AWS API Gateway & AWS Cognito

## Overview

This project demonstrates the creation of a simple calculator application using AWS Lambda, API Gateway, Django, and AWS Cognito for user authentication. The calculator multiplies two numbers, and the application is accessible through both a serverless AWS Lambda endpoint and a Django web interface.

## Steps to Reproduce

### 1. AWS Lambda Function

- Created an AWS Lambda function using the following code in Python:

```python
import json

def lambda_function(operand1, operand2):
    # Simple multiplication operation
    result = operand1 * operand2
    return result

def lambda_handler(event, context):
    operand1 = float(event['queryStringParameters']['operand1'])
    operand2 = float(event['queryStringParameters']['operand2'])
    result = lambda_function(operand1, operand2)

    return {
        'statusCode': 200,
        'body': json.dumps({'operand1': operand1, 'operand2': operand2, 'result': result})
    }
```

________________


### 2. AWS API Gateway & Creating Django Project Locally

#### AWS API Gateway:

- Deployed an API Gateway and created an endpoint with the following URL:
`https://1kzlnygkfc.execute-api.eu-north-1.amazonaws.com/Demo/Lambda_function?operand1=2&operand2=13`
- The endpoint takes two query parameters (`operand1` and `operand2`) and returns the product of multiplication.

#### Creating Django Project Locally to connect with AWS:
- Developed a Django project to create a local web interface for the calculator the two operand after we added http://127.0.0.1:8000 connecting with AWS .
- Created a Django app named "lambda" and added necessary templates (`Lambda_function.html`, `login.html`, `logged_out.html`, and `index.html`).
- The multiplication functionality is implemented in the Django view.


## - Lambda_function.html

### Overview:

The `Lambda_function.html` file is a Django template designed for a straightforward calculator application. Here's a concise summary of its key features:

### Features:

1. **User-Friendly Interface:**
   - Provides an intuitive form with input fields for two operands and a "Calculate" button.

2. **JavaScript Functionality:**
   - Incorporates a JavaScript function triggered by the "Calculate" button.
   - Retrieves user-input operand values.

3. **AWS Lambda Interaction:**
   - Constructs a POST request to an AWS Lambda function endpoint for calculation.
   - Expects a JSON response containing the calculated result.

4. **Result Display:**
   - Dynamically showcases the calculated result on the webpage.

5. **CORS Handling:**
   - Includes CORS headers in the API request for seamless cross-origin communication.
   - Configures the AWS Lambda function endpoint (`apiUrl`) and `Origin` header.

### User Experience:

Users can easily input numerical values, initiate the calculation process, and promptly view the result. The template streamlines the interaction with an AWS Lambda function, offering a smooth and efficient calculator experience.

Feel free to integrate this template into your Django project, enhancing it with a user-friendly calculator functionality. Note that the actual AWS Lambda function logic is not provided in this snippet.

### Image of the output:

<img src="https://github.com/hamzaderbaz/AWS-Lambda-Function/assets/51893602/de8ed7f8-cb83-4e72-9732-48895d8d2bc5" width="50%" />

________________


### 3. AWS Cognito Integration

- Set up AWS Cognito to implement user authentication for the Django project.
- Configured Django to use AWS Cognito for user authentication.
- Created additional templates (`login.html`, `logged_out.html`, and `index.html`) within the Django project for user authentication and authorization.

### Image of the output:

<img src="https://github.com/hamzaderbaz/AWS-Lambda-Function/assets/51893602/92789cae-3b7c-41a4-b553-96aee856db25" width="50%" />
<img src="https://github.com/hamzaderbaz/AWS-Lambda-Function/assets/51893602/0f2e2089-c773-4e63-be62-0de4edac683d" width="50%" />


## Running the Django Project Locally

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Apply migrations:

   ```bash
   python manage.py migrate
   ```

3. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at [http://127.0.0.1:8000/lambda/my_lambda/](http://127.0.0.1:8000/lambda/my_lambda/).

## Notes

- Ensure AWS credentials are properly configured for AWS Lambda and API Gateway deployment.
- Update AWS Cognito configuration in Django settings for proper authentication.

Feel free to reach out if you have any questions or encounter issues.

---

This README file provides a comprehensive guide for users to understand the project, replicate the steps, and run the Django project locally. Adjust the content as needed based on specific details and preferences.