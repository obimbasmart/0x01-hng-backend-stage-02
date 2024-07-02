# Basic web server
Setup a basic web server in your preffered stack. Deploy it to any free hosting platform and expose an API endpoint that comforms to the criteria below:

- Endpoint: [`GET`] `<example.com>/api/hello?visitor_name=Mark`. (where `example.com` is your server origin)

- Response:
    ```
        {
            "client_pi": 127.0.0.1  // The IP of the requester,
            "location": New york, // The city of the reqeuster
            "greeting": "Hello, Mark!, the temperature is 11 degrees Celcuis in New York"
        }
    ```

### How to submit:
- Host your API on some free hosting service