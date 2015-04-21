from haystack.forms import SearchForm


class NotesSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()