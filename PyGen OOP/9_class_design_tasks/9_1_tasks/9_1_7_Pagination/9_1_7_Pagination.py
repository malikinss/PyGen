'''
TODO:
    Implement the Pagination class to handle paginated data.

    Pagination is used to split a large amount of data into chunks.

    A Pagination class instance should be created based on two values:
        - the original data, represented as a list with arbitrary elements
        - the page size, i.e. the number of elements to display on each page

        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        pagination = Pagination(alphabet, 4)

    The get_visible_items() method should be used to get the page contents:
        print(pagination.get_visible_items()) # ['a', 'b', 'c', 'd']

    Note that the page contents should be represented as a list.

    The following methods should be used to navigate through pages:
        prev_page() — return to the previous page
        next_page() — go to the next page
        first_page() — return to the first page
        last_page() — go to the last page
        go_to_page() — go to the page with the specified number
                       (1 — the first page, 2 — the second page, and so on)

        pagination.next_page()
        print(pagination.get_visible_items()) # ['e', 'f', 'g', 'h']
        pagination.last_page()
        print(pagination.get_visible_items()) # ['y', 'z']

    The methods for navigating through pages should be applied one after
    another:
        pagination.first_page()
        pagination.next_page().next_page()
        print(pagination.get_visible_items()) # ['i', 'j', 'k', 'l']

    With the total_pages and current_page attributes it should be possible to
    get the total number of pages and the current page respectively:
        print(pagination.total_pages) # 7
        print(pagination.current_page) # 3

    When on the first page and moving to the previous page, the current page
    should remain the first page.

    Similarly, when on the last page and moving to the next page, the current
    page should remain the last page:
        pagination.first_page()
        pagination.prev_page()
        print(pagination.get_visible_items()) # ['a', 'b', 'c', 'd']
        pagination.last_page()
        pagination.next_page()
        print(pagination.get_visible_items()) # ['y', 'z']

    When moving to page zero or less, the current page should become the first
    page.

    Similarly, when moving to a page whose number exceeds the total number of
    pages, the current page should be the last page:
        pagination.go_to_page(-100)
        print(pagination.get_visible_items()) # ['a', 'b', 'c', 'd']
        pagination.go_to_page(100)
        print(pagination.get_visible_items()) # ['y', 'z']
'''
