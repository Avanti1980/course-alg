({
  // Please visit the URL below for more information:
  // https://shd101wyy.github.io/markdown-preview-enhanced/#/extend-parser

  onWillParseMarkdown: async function(markdown) {
    markdown = markdown.replace(
      /我的批注/g,
      (whole, content) => '<span class="yellow">:fa-weixin:</span>'
    );
    markdown = markdown.replace(
      /我的启示/g,
      (whole, content) => '<span class="blue">:fa-lightbulb-o:</span>'
    );
    return markdown;
  },

  onDidParseMarkdown: async function(html) {
    return html;
  },
})