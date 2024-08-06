# Experience

Add a brief description of this project here, in Markdown format.
It will be shown on the main page of the project's GitHub repository.

## Development

To work on this project in a scratch org:

1. [Set up CumulusCI](https://cumulusci.readthedocs.io/en/latest/tutorial.html)
2. Run `cci flow run dev_org --org dev` to deploy this project.
3. Run `cci org browser dev` to open the org in your browser.

## Delivery

To release a new version of this project:

1. Check out the `main` branch in your local dev environment.
2. Run `git fetch origin` followed by `git pull` to ensure the latest commits are captured locally.
3. Run `cci flow run dependencies --org dev` to prepare a "Packaging Org".
4. Run `cci flow run release_unlocked_beta --org dev --debug` to generate a new beta release.
5. Run `cci flow run release_unlocked_prod --org dev --debug` to promote the latest beta release.