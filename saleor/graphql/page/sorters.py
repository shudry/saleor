import graphene

from ..core.types import SortInputObjectType


class PageSortField(graphene.Enum):
    TITLE = ["title", "slug"]
    SLUG = ["slug"]
    VISIBILITY = ["is_published", "title", "slug"]
    CREATION_DATE = ["created", "title", "slug"]
    PUBLICATION_DATE = ["publication_date", "title", "slug"]

    @property
    def description(self):
        # pylint: disable=no-member
        if self in [
            PageSortField.TITLE,
            PageSortField.SLUG,
            PageSortField.VISIBILITY,
            PageSortField.CREATION_DATE,
            PageSortField.PUBLICATION_DATE,
        ]:
            sort_name = self.name.lower().replace("_", " ")
            return f"Sort pages by {sort_name}."
        raise ValueError("Unsupported enum value: %s" % self.value)


class PageSortingInput(SortInputObjectType):
    class Meta:
        sort_enum = PageSortField
        type_name = "pages"
