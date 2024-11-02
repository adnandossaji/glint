# Glint

Glint is a static site generator that allows you to create a website using React and YAML. Inspired by Jekyll, Glint provides a streamlined approach to generating static sites with dynamic capabilities through React components.

## Features

- **React Components**: Leverage the power of React to create interactive and reusable components for your site.
- **YAML Content**: Easily define your site's content using YAML files, making it simple to manage posts, pages, and metadata.
- **Automatic HTML Generation**: Glint automatically generates HTML files from your YAML content, allowing you to focus on design and functionality.
- **Layouts**: Define layouts using React components to ensure a consistent look and feel across your site.
- **Markdown Support**: Write your content in Markdown, and Glint will convert it to HTML for display on your site.
- **Customizable**: Modify the layout and styles to fit your brand and design requirements.

## Installation

To install Glint, use pip:

```bash
pip install glint
```

## Usage

1. **Create a New Project**: Start by creating a new directory for your project and initializing it with Glint.

    ```bash
    mkdir my-glint-site
    cd my-glint-site
    glint generate
    ```

2. **Add Content**: Create YAML files in the `_posts` directory. Each file should follow the naming convention `YYYY-MM-DD-title.yaml` and contain the following structure:

    ```yaml
    title: "Welcome to Glint"
    date: "2024-11-01"
    content: |
      # Welcome to Glint
      This is your first post!
    ```

3. **Create Layouts**: Define your layout in the `layouts` directory. Create a file called `default.tsx` with the following example content:

    ```tsx
    import React from 'react';

    const DefaultLayout = ({ children }) => {
        return (
            <html>
                <head>
                    <title>My Glint Site</title>
                </head>
                <body>
                    <div>{children}</div>
                </body>
            </html>
        );
    };

    export default DefaultLayout;
    ```

4. **Build Your Site**: Run the following command to generate the static files:

    ```bash
    python -m glint.cli generate
    ```

5. **View Your Site**: Open the generated HTML files located in the `dist` directory in your browser to see your new site in action.

## Contributing

Contributions are welcome! To help you get started with contributing to Glint, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right of the Glint GitHub page to create your own copy of the repository.

2. **Clone Your Fork**: Clone your forked repository to your local machine:

    ```bash
    git clone https://github.com/your-username/glint.git
    cd glint
    ```

3. **Set Up the Project**: Install the required dependencies using npm:

    ```bash
    npm install
    ```

4. **Build the Project**: After installing the dependencies, build the project to ensure everything is set up correctly:

    ```bash
    npm run build
    ```

5. **Create a New Branch**: Create a new branch for your feature or bug fix:

    ```bash
    git checkout -b your-feature-branch
    ```

6. **Make Your Changes**: Implement your changes or features in the code.

7. **Commit Your Changes**: After making your changes, commit them with a clear message:

    ```bash
    git add .
    git commit -m "Brief description of your changes"
    ```

8. **Push Your Branch**: Push your changes to your forked repository:

    ```bash
    git push origin your-feature-branch
    ```

9. **Submit a Pull Request**: Go to the original Glint repository on GitHub, and you should see an option to create a pull request from your branch. Provide a clear description of the changes you made.

Thank you for contributing to Glint!


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
