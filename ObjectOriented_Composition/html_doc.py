class Tag:

    def __init__(self, name, contents=''):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)  # it's actually calling the __str__ method


class DocType(Tag):
    """ Extension (sub class) of Tag """

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd')
        self.end_tag = ''  # DOCTYPE doesn't have an end tag


class Head(Tag):
    """ Extension (sub class) of Tag
    The title will appear in the browser tab bar """

    def __init__(self, title=None):
        super().__init__('HEAD')
        if title:
            self._title_tag = Tag('TITLE', title)
            self.contents = str(self._title_tag)


class Body(Tag):
    """ Extension (sub class) of Tag """

    def __init__(self):
        super().__init__('BODY')  # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)  # COMPOSITION
        # assigning a class to a data attribute, Tag object doesn't exist outside of the Body object
        self._body_contents.append(new_tag)  # adds the Tag object to the body contents list

    def display(self, file=None):  # overriding the method from super class
        for tag in self._body_contents:
            # print(tag)
            # print(type(tag))
            self.contents += str(tag)  # equivalent to calling tag.__str__()

        super().display(file=file)


class HtmlDoc:
    """ HtmlDoc is composed out of other classes
    Those objects only exists inside Html object """

    def __init__(self, title=None):
        self._doc_type = DocType()  # COMPOSITION
        self._head = Head(title)  # COMPOSITION
        self._body = Body()  # COMPOSITION

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)  # delegation

    def display(self, file=None):  # delegation again for all the displays
        self._doc_type.display(file=file)
        print('<HTML>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</HTML>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc('Demo HTML Document')
    my_page.add_tag('H1', 'Main Heading')
    my_page.add_tag('H2', 'Sub-Heading')
    my_page.add_tag('P', 'This is a paragraph that will appear on the page')
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)

    # AGGREGATION
    new_body = Body()  # we first create the object that is going to be aggregated
    new_body.add_tag('H1', 'Aggregation')
    new_body.add_tag('P', 'Unlike <strong>composition</strong>, aggregation uses existing instances'
                          ' of objects to build up another object.')
    new_body.add_tag('P', 'The composed object doesn\'t actually own the objects that it\'s composed of'
                          ' - if it\'s destroyed, those objects continue to exist.')

    # give our document new content by switching it's body
    my_page._body = new_body  # here we aggregate the object created above to another object
    with open('test2.html', 'w') as test_doc:
        my_page.display(file=test_doc)
