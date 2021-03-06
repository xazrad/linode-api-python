Pagination
==========

The Linode API V4 returns collections of resources one page at a time.  While
this is useful, this library abstracts away the details of pagination and makes
collections of resources appear as a single, uniform list that can be accessed,
iterated over, and indexed as any normal Python list would be::

   regions = client.get_regions() # get a collection of Regions

   for region in regions:
       print(region.id)

   first_region = regions[0]
   last_region = regions[-1]

Pagination is handled transparently, and as requested.  For example, if you had
three pages of Linodes, accessing your collection of Linodes would behave like
this::

   linodes = client.linode.get_instances() # loads the first page only

   linodes[0] # no additional data is loaded

   linodes[-1] # third page is loaded to retrieve the last Linode in the collection

   for linode in linodes:
       # the second page will be loaded as soon as the first Linode on that page
       # is required.  The first and third pages are already loaded, and will not
       # be loaded again.
       print(linode.label)

The first page of a collection is always loaded when the collection is
returned, and subsequent pages are loaded as they are required.  When slicing
a paginated list, only the pages required for the slice are loaded.

PaginatedList class
-------------------

.. autoclass:: linode.PaginatedList
   :members: first, only, last
