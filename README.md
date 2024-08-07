# Experience


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
