from docutils import nodes
from docutils.parsers.rst import Directive, directives

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

class checkbox(nodes.Body, nodes.Element):
    pass

def visit_checkbox_node(self, node):
    print(">> Visit checkbox Node!")

def depart_checkbox_node(self, node):
    print(">> Depart checkbox Node!")

def checked(argument):
    print("argument is " + argument)
    if (argument is not "yes"):
        return ''
    return 'checked'

class CheckboxDirective(SphinxDirective):

    has_content = True
    optional_arguments = 2
    option_spec = { 'checked': checked }

    def run(self):
        targetid = 'checkbox-%d' % self.env.new_serialno('checkbox')
        targetnode = nodes.target('', '', ids=[targetid])

        checkbox_node = checkbox(self.content)
        checkbox_node.options = self.options
        self.state.nested_parse(self.content, self.content_offset, checkbox_node)
        #print(self.options['checked'])
        return [targetnode, checkbox_node]


def html_checkbox(self, node):
    template= """
        <div class=\"checkbox\"><input type=\"checkbox\" %(checked)s ><label>
        %(content)s
        </label></div>
    """
    print(str(node))
    self.body.append(template%{'content':str(node), 'checked':str(node.options['checked'])})
    raise nodes.SkipNode


def purge_cbs(app, env, docname):
    if not hasattr(env, 'checkbox_all_checkboxes'):
        return

    env.checkbox_all_checkboxes = [cb for cb in env.checkbox_all_checkboxes
                                    if cb['docname'] != docname]


def process_checkbox_nodes(app, doctree, fromdocname):
    if not app.config.include_checkbox:
        for node in doctree.traverse(checkbox):
            node.parent.remove(checkbox)

    env = app.builder.env

    for node in doctree.traverse(checkbox):
        if not app.config.include_checkbox:
            node.replace_self([])
            continue

        content = []
        content.append(node)

        node.replace_self(content)


def setup(app):
    app.add_config_value('include_checkbox', False, 'html')

    app.add_node(checkbox,
                html=(html_checkbox, depart_checkbox_node),
                text=(visit_checkbox_node, depart_checkbox_node)
                #latex=(visit_checkbox_node, depart_checkbox_node)
                )
    app.add_directive('checkbox', CheckboxDirective)
    app.connect('doctree-resolved', process_checkbox_nodes)
    app.connect('env-purge-doc', purge_cbs)

    return {'version' : '0.1'}  # identifies the version of our extension
