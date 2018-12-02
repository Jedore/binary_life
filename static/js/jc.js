// convert markdown string to html
function markdown_to_html(text, if_toc) {
  let renderer = new marked.Renderer();
  let toc = [];
  renderer.heading = function (text, level, raw) {
    let anchor = this.options.headerPrefix + raw.toLowerCase();
    if (if_toc) {
      toc.push({
        anchor: anchor,
        level: level,
        text: text,
        children: [],
      });
    }
    return '<h'
        + level
        + ' id="'
        + anchor
        + '">'
        + text
        + '</h'
        + level
        + '>\n';
  };
  renderer.link = function (href, title, text) {
    let link = marked.Renderer.prototype.link.call(this, href, title, text);
    return link.replace("<a", "<a target='_blank' ");
  };
  marked.setOptions({
    renderer: renderer,
    breaks: true,
    smartLists: true,
  })
  return {
    'html': marked(text),
    'toc': toc,
  };
}

function reply(event, reply_id) {
  $("#commit .cancel-reply").attr("hidden", false);
  $("#commit #reply-id").val(reply_id);
  $("#commit").insertAfter((event.parentNode));
}

function cancel_reply() {
  $("#commit").insertAfter(($("#comment-list")));
  $("#commit .cancel-reply").attr("hidden", true);
  $("#commit #reply-id").val("");
}

function reset_commit() {
  $("#commit").insertAfter(($("#comment-list")));
  $("#commit .cancel-reply").attr("hidden", true);
  $("#commit #reply-id").val("");
  $("#commit #comment").val("");
  $("#commit #name").val("");
}

