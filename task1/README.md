# hngx_task1
## :dart: Objective

Create and host an endpoint using any programming language of your choice. The endpoint should take two GET request query parameters and return specific information in JSON format.<br>
The endpoint should accept two GET request query parameters: slack_name and track.<br>
       E.g.: http://example.com/api?slack_name=example_name&track=backend.

## &#128220; Requirements

The information required includes:

- Slack name
- Current day of the week
- Current UTC time (with validation of +/-2)
- Track
- The GitHub URL of the file being run
- The GitHub URL of the full source code.
- A Status Code of Success

<b> The endpoint's response should be something like this:<b> <br>
```json
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}
