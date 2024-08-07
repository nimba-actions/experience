# Experience Project

This project automates the setup and deployment of a Salesforce Digital Experience (formerly known as Community).

## What This Does

1. **Creates a Digital Experience Site**: 
   - Sets up a new Digital Experience site in your Salesforce org.
   - Uses a predefined template (defaults to "Customer Service").
   - Customizes the site name and URL prefix.

2. **Configures User Access**:
   - Designates the default Scratch Org user as the "Community Owner".
   - Sets up a Community User.
   - Configures a Network Member Group record.

3. **Enhances User Interface**:
   - Adds a "Log in as User" button to the standard Contact layout, improving admin usability.

4. **Loads Sample Data**:
   - Populates the Experience with sample data, providing a realistic environment for testing or demonstration.

5. **Automates Deployment Process**:
   - Includes pre-deployment steps to set up the basic structure and configuration.
   - Performs post-deployment tasks to finalize the setup, including publishing the Experience site.

6. **Ensures Consistency Across Environments**:
   - Provides optional flows for configuring both development and managed package environments.
   - Uses environment variables to maintain consistency in naming and configuration across different orgs.

This configuration streamlines the process of setting up a fully functional Salesforce Digital Experience in Scratch, Sandbox, or Production environments.


## Usage

### 1. Paste the following into the "root" section of your cumulusci.yml

```yml
sources:
    experience:
        github: https://github.com/nimba-actions/experience
        allow_remote_code: True
```

### 2. Paste the following sections into the "tasks" section of your cumulusci.yml file

```yml
    make_experience_cli:
        class_path: cumulusci.tasks.command.Command
        options:
            command: "cci flow run make_experience --org dev --debug -o env__name YOUR_EXPERIENCE_API_NAME -o env__url_prefix YOUR_EXPERIENCE_URL_PREFIX"

    deploy_experience_cloud:
        group: "experience"
        description: Deploys the Experience Bundle and other related metadata to the target org
        class_path: cumulusci.tasks.salesforce.Deploy
        options:
            path: "unpackaged/config/experience" # change this to whatever you want
```
### 3. Paste the following sections into the "flows" section of your cumulusci.yml file
```yml
    make_experience:
        steps:
            1:
                flow: experience:deploy_pre
            2:
                task: deploy_experience_cloud
            3:
                flow: experience:deploy_post
```

```yml
    # [OPTIONAL]
    config_dev: 
        steps:
            3:   
                task: make_experience_cli
            4:
                task: assign_unpackaged_permission_sets
```

```yml
    # [OPTIONAL]
    config_managed:
        steps:
            3:
                task: make_experience_cli
            4:
                task: assign_unpackaged_permission_sets
```

### 4. Retrieve your ExperienceBundle, Network, StaticResources, etc to `unpackaged/config/experience` (or whatever path you specified in `deploy_experience_cloud`)

### 5. Voila! 
