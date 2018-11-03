from django import template
from django.utils.safestring import mark_safe


register = template.Library()
def comment_sublevel(comment_1,margin_left):
    html = ''
    for k,v in comment_1.items():
        html += '<div style="margin-left:%spx">'%margin_left+'<div style=color:red>'+k.username+'&nbsp'+'&nbsp'+':'+'</div>'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+k.content+'</div>'
        if v:
            html += comment_sublevel(v,margin_left+20)
    return html
def comment1(comments,comment):
    for p,v in comments.items():
        if p == comment.parent_cmt:
            comments[p][comment] = {}
            break
        else:
            comment1(comments[p],comment)


@register.simple_tag
def comment_tree(comment_list):
    comments ={}
    for i in comment_list:
        if i.parent_cmt is None:
            comments[i]={}
        else:
            comment1(comments,i)


    html = '<div>'
    margin_left = 0
    for k,v in comments.items():
        html +='<div>' '<div style=color:red>'+k.username+'&nbsp'+'&nbsp'+':'+'</div>'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+'&nbsp'+k.content+ '</div>'
        html += comment_sublevel(v,margin_left+20)

    html+= '</div>'
    return mark_safe(html)