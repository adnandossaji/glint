const React = require('react');
const ReactDOMServer = require('react-dom/server');
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const DefaultLayout = require('./glint_dist/layouts/default.js').default;

function renderLayout(data) {
    const content = ReactDOMServer.renderToStaticMarkup(
        React.createElement(DefaultLayout, data)
    );
    return '<!DOCTYPE html>' + content;
}

function readYAML(filePath) {
    return yaml.load(fs.readFileSync(filePath, 'utf8'));
}

const args = process.argv.slice(2);
const yamlFilePath = args[0];
const postData = readYAML(yamlFilePath);
const html = renderLayout({ title: postData.title, content: postData.content });
fs.writeFileSync(path.resolve('dist', `${postData.date}-${postData.title.replace(/\s+/g, '_')}.html`), html);
