class JSScript:
    SCROLL_TO_TOP = "window.scrollTo(0, 0)"
    SCROLL_INTO_VIEW = "arguments[0].scrollIntoView(true);"
    REMOVE_ELEMENT = '''
            var element = arguments[0];
            element.parentNode.removeChild(element);
            '''
