def cakeSet():
    print '1 cup butter, softened'
    print '3 cups packed brown sugar'
    print '4 large eggs'
    print '2 teaspoons vanilla extract'
    print '2-2/3 cups all-purpose flour'
    print '3/4 cup baking cocoa'
    print '3 teaspoons baking soda'
    print '1/2 teaspoon salt'
    print '1-1/3 cups sour cream'
    print '1-1/3 cups boiling water'
    print
    print 'FROSTING:'
    print '1/2 cup butter, cubed'
    print '3 ounces unsweetened chocolate, chopped'
    print '3 ounces semisweet chocolate, chopped'
    print "5 cups confectioners' sugar"
    print '1 cup (8 ounces) sour cream'
    print '2 teaspoons vanilla extract'
    print
    print 'Preheat oven to 350�X. Grease and flour three 9-in. round baking pans.'
    print 'In a large bowl, cream butter and brown sugar until light and fluffy.'
    print 'Add eggs, one at a time, beating well after each addition.'
    print 'Beat in vanilla. In another bowl, whisk flour, cocoa, baking soda and salt;'
    print 'add to creamed mixture alternately with sour cream, beating well after each addition.'
    print 'Stir in water until blended.'
    print
    print 'Transfer to prepared pans. Bake 30-35 minutes or until a toothpick inserted in center comes out clean.'
    print 'Cool in pans 10 minutes before removing to wire racks to cool completely.'
    print 
    print 'For frosting, in a metal bowl over simmering water, melt butter and chocolates; stir until smooth. Cool slightly.'
    print "In a large bowl, combine confectioners' sugar, sour cream and vanilla."
    print 'Add chocolate mixture; beat until smooth. Spread frosting between layers and over top and sides of cake. '
    print 'Refrigerate leftovers. Yield: 16 servings.'
def cookieSet():
    print 'flour, chocolate chips, sugar'
def muffinSet():
    print 'flour, yeast, sugar, seasalt, eggs'
print 'Welcome to bakery. What set do you want to buy?'
print 'We have cake set, cookie set, and muffin set.'
while (True):
    get = raw_input()
    if (get == 'cake'):
        cakeSet()
    elif (get == 'cookie'):
        cookieSet()
    elif (get == 'muffin'):
        muffinSet()
      

