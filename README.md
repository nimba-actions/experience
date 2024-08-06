# Experience


### 1. Paste the following into the "root" section of your cumulusci.yml

```
sources:
    experience:
        github: https://github.com/nimba-actions/experience
        allow_remote_code: True
```

### 2. Paste the following section into the "tasks" section of your cumulusci.yml file

```
    
    deploy_experience_cloud:
        group: "experience"
        description: Deploys the Experience Bundle and other related metadata to the target org
        class_path: cumulusci.tasks.salesforce.Deploy
        options:
            path: "unpackaged/config/experience"
```
### 3. Paste the following section into the "flows" section of your cumulusci.yml file

``` 
    make_experience:
        steps:
            1:
                flow: experience:deploy_pre
            2:
                task: deploy_experience_cloud
            3:
                flow: experience:deploy_post
```

### 4. Run the following command - options must be provided via CLI for now :(

```
cci flow run make_experience --org dev --debug -o env__name "My_Experience_Api_Name" -o env__url_prefix "my-url-prefix"
```