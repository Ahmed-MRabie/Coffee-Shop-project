class Pagination:

    def __init__(self, items=[], page_size=10):
        """Initialize attributes to describe the Coffee Shop"""
        page_size = int(page_size)
        
        self.items = items
        self.page_size = page_size
        # To be current page is first page by default
        self.start_point = 0
        self.end_point = page_size

    #=======================================================================================================
    def getVisibleItems(self):
        """Return items of current page"""
        return self.items[self.start_point:self.end_point]

    #=======================================================================================================
    def nextPage(self):
        """Point to next page items"""
        if self.end_point >= len(self.items):
            self.lastPage()
        else:
            self.start_point = self.end_point
            self.end_point += self.page_size
        return self

    #=======================================================================================================
    def prevPage(self):
        """Point to previous page items"""
        if self.start_point == 0:
            self.firstPage()
        else:
            self.end_point = self.start_point 
            self.start_point -= self.page_size
        return self

    #=======================================================================================================
    def firstPage(self):
        """Point to first page items"""
        self.start_point = 0
        self.end_point = self.page_size
        return self

    #=======================================================================================================
    def lastPage(self):
        """Point to first page items"""
        if len(self.items) % self.page_size == 0:
            self.start_point = len(self.items) - self.page_size
            self.end_point = len(self.items)
        else:
            #self.start_point = round(len(self.items) / self.page_size) * self.page_size
            self.start_point = len(self.items) - (len(self.items) % self.page_size)
            self.end_point = len(self.items)
        return self

    #=======================================================================================================
    def goToPage(self, page_num):
        """Point to input page number items"""
        pages = len(self.items) / self.page_size
        
        if page_num <= 0 or page_num == 1:
            self.firstPage()
        elif page_num > round(pages):
            self.lastPage()
        else:
            self.start_point = (page_num - 1) * self.page_size
            self.end_point = self.start_point + self.page_size
        #elif page_num == 3:
         #   self.start_point = 2 * self.page_size
          #  self.end_point = self.start_point + self.page_size
        return self