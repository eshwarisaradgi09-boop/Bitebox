from delivery.models import Restaurant, Item

def seed():

    restaurants = {

        "KFC": [

            {
                "name": "Chicken Zinger Burger",
                "description": "Crispy chicken fillet burger with lettuce and creamy mayo.",
                "price": 199,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
            },
            {
                "name": "Hot & Crispy Chicken",
                "description": "Original crispy fried chicken pieces.",
                "price": 249,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58"
            },
            {
                "name": "Chicken Popcorn",
                "description": "Bite-sized crispy chicken popcorn.",
                "price": 179,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1606755962773-d324e0a13086"
            },
            {
                "name": "Chicken Bucket",
                "description": "8 pieces of signature crispy chicken.",
                "price": 699,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1513639776629-7b61b0ac49cb"
            },
            {
                "name": "Chicken Wings",
                "description": "Spicy crispy chicken wings.",
                "price": 269,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1527477396000-e27163b481c2"
            },
            {
                "name": "Chicken Wrap",
                "description": "Soft tortilla filled with crispy chicken and veggies.",
                "price": 199,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1539252554453-80ab65ce3586"
            },
            {
                "name": "Veg Burger",
                "description": "Crispy vegetable burger with cheese.",
                "price": 149,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1525059696034-4967a8e1dca2"
            },
            {
                "name": "Cheese Fries",
                "description": "French fries topped with melted cheese.",
                "price": 149,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1585109649139-366815a0d713"
            },
            {
                "name": "Chicken Rice Bowl",
                "description": "Rice bowl served with spicy chicken gravy.",
                "price": 219,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1512058564366-18510be2db19"
            },
            {
                "name": "Chicken Strips",
                "description": "Crunchy boneless chicken strips.",
                "price": 229,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1562967916-eb82221dfb36"
            },
            {
                "name": "Pepsi",
                "description": "500ml chilled Pepsi.",
                "price": 60,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1629203851122-3726ecdf080e"
            },
            {
                "name": "Chocolate Sundae",
                "description": "Vanilla ice cream with chocolate syrup.",
                "price": 129,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1563805042-7684c019e1cb"
            },
            {
                "name": "Chocolate Brownie",
                "description": "Warm chocolate brownie.",
                "price": 139,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c"
            },
            {
                "name": "Chicken Combo Meal",
                "description": "Burger, fries and Pepsi combo.",
                "price": 399,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1550547660-d9450f859349"
            }

        ],

        "Spice Garden": [

            {
                "name": "Paneer Butter Masala",
                "description": "Paneer cubes cooked in creamy tomato butter gravy.",
                "price": 249,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7"
            },
            {
                "name": "Butter Chicken",
                "description": "Tender chicken cooked in buttery tomato gravy.",
                "price": 329,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8YnV0dGVyJTIwY2hpY2tlbnxlbnwwfHwwfHx8MA%3D%3D"
            },
            {
                "name": "Chicken Biryani",
                "description": "Hyderabadi style chicken biryani.",
                "price": 299,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1716550781939-beb7d7247aae?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2hpY2tlbiUyMGJpcml5YW5pfGVufDB8fDB8fHww"
            },
            {
                "name": "Veg Biryani",
                "description": "Flavorful basmati rice with vegetables.",
                "price": 229,
                "vegeterian": True,
                "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvVqxfmsUlXci4Gq_0qCR1iZgxxRKitcH5m_9uj7LPlw&s=10"
            },
            {
                "name": "Palak Paneer",
                "description": "Paneer cooked in spinach gravy.",
                "price": 239,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1589647363585-f4a7d3877b10?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cGFsYWslMjBwYW5lZXJ8ZW58MHx8MHx8fDA%3D"
            },
            {
                "name": "Dal Makhani",
                "description": "Slow cooked black lentils with butter.",
                "price": 199,
                "vegeterian": True,
                "picture": "https://plus.unsplash.com/premium_photo-1700752343809-6dc1517295df?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZGFsJTIwbWFraGFuaXxlbnwwfHwwfHx8MA%3D%3D"
            },
            {
                "name": "Shahi Paneer",
                "description": "Paneer in rich cashew gravy.",
                "price": 259,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7"
            },
            {
                "name": "Chicken Tikka",
                "description": "Juicy grilled chicken marinated with Indian spices.",
                "price": 289,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2hpY2tlbiUyMHRpa2thfGVufDB8fDB8fHww"
            },
            {
                "name": "Tandoori Chicken",
                "description": "Charcoal grilled spicy chicken.",
                "price": 349,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1603360946369-dc9bb6258143"
            },
            {
                "name": "Garlic Naan",
                "description": "Soft naan topped with garlic butter.",
                "price": 69,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1559561724-4ea348cd867f?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Z2FybGljJTIwbmFhbnxlbnwwfHwwfHx8MA%3D%3D"
            }
        ],

                "Pizza Palace": [

            {
                "name": "Margherita Pizza",
                "description": "Classic pizza with mozzarella cheese and tomato sauce.",
                "price": 299,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1604382355076-af4b0eb60143"
            },
            {
                "name": "Farmhouse Pizza",
                "description": "Loaded with fresh vegetables and mozzarella cheese.",
                "price": 379,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1513104890138-7c749659a591"
            },
            {
                "name": "Veg Supreme Pizza",
                "description": "Capsicum, onion, olives, corn and mushrooms.",
                "price": 399,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1594007654729-407eedc4be65"
            },
            {
                "name": "Pepperoni Pizza",
                "description": "Classic pepperoni pizza with mozzarella cheese.",
                "price": 449,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1628840042765-356cda07504e"
            },
            {
                "name": "Chicken Dominator",
                "description": "Loaded with grilled chicken and cheese.",
                "price": 499,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1513104890138-7c749659a591"
            },
            {
                "name": "Paneer Tikka Pizza",
                "description": "Paneer tikka with onions and capsicum.",
                "price": 429,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1513104890138-7c749659a591"
            },
            {
                "name": "Cheese Burst Pizza",
                "description": "Pizza stuffed with molten cheese.",
                "price": 449,
                "vegeterian": True,
                "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHUEadDvH5d9XlBgYfSBXa5gZGTFWii3VUdNzWoeLVzA&s=10"
            },
            {
                "name": "Garlic Bread",
                "description": "Fresh garlic bread with herbs.",
                "price": 149,
                "vegeterian": True,
                "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpRE1eKdH1mjPf1xqb2yQqBV0VhHxsP5_sWn8AyhA_WQ&s=10"
            },
            {
                "name": "Stuffed Garlic Bread",
                "description": "Garlic bread stuffed with cheese.",
                "price": 199,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1509440159596-0249088772ff"
            },
            {
                "name": "Veg White Sauce Pasta",
                "description": "Creamy white sauce pasta with vegetables.",
                "price": 229,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9"
            },
            {
                "name": "Chicken Alfredo Pasta",
                "description": "Creamy Alfredo pasta with grilled chicken.",
                "price": 279,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1555949258-eb67b1ef0ceb"
            },
            {
                "name": "Veg Lasagna",
                "description": "Layers of pasta, vegetables and cheese.",
                "price": 319,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1619895092538-128341789043"
            },
            {
                "name": "Chocolate Lava Cake",
                "description": "Warm chocolate cake with molten center.",
                "price": 129,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1563729784474-d77dbb933a9e"
            },
            {
                "name": "Coke",
                "description": "300ml chilled Coca-Cola.",
                "price": 60,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1554866585-cd94860890b7"
            },
            {
                "name": "Brownie with Ice Cream",
                "description": "Warm brownie served with vanilla ice cream.",
                "price": 179,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c"
            }

        ],

                "Burger Hub": [

            {
                "name": "Classic Veg Burger",
                "description": "Crispy vegetable patty with lettuce and cheese.",
                "price": 149,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1525059696034-4967a8e1dca2"
            },
            {
                "name": "Classic Chicken Burger",
                "description": "Juicy grilled chicken burger with mayo.",
                "price": 199,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
            },
            {
                "name": "Double Cheese Burger",
                "description": "Double cheese with crispy veg patty.",
                "price": 249,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1550547660-d9450f859349"
            },
            {
                "name": "BBQ Chicken Burger",
                "description": "Chicken burger with smoky BBQ sauce.",
                "price": 259,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1571091718767-18b5b1457add"
            },
            {
                "name": "Spicy Paneer Burger",
                "description": "Paneer patty with spicy sauce.",
                "price": 189,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1550547660-d9450f859349"
            },
            {
                "name": "Chicken Cheese Burger",
                "description": "Grilled chicken topped with melted cheese.",
                "price": 239,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
            },
            {
                "name": "French Fries",
                "description": "Golden crispy potato fries.",
                "price": 99,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877"
            },
            {
                "name": "Cheese Fries",
                "description": "French fries loaded with melted cheese.",
                "price": 149,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1585109649139-366815a0d713"
            },
            {
                "name": "Chicken Nuggets",
                "description": "Crispy chicken nuggets served with dip.",
                "price": 179,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1606755962773-d324e0a13086"
            },
            {
                "name": "Onion Rings",
                "description": "Golden fried onion rings.",
                "price": 129,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec"
            },
            {
                "name": "Veg Wrap",
                "description": "Fresh vegetables wrapped in a soft tortilla.",
                "price": 169,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1539252554453-80ab65ce3586"
            },
            {
                "name": "Chicken Wrap",
                "description": "Grilled chicken wrapped with fresh veggies.",
                "price": 209,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1539252554453-80ab65ce3586"
            },
            {
                "name": "Chocolate Milkshake",
                "description": "Rich chocolate milkshake.",
                "price": 159,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1572490122747-3968b75cc699"
            },
            {
                "name": "Cold Coffee",
                "description": "Refreshing chilled coffee.",
                "price": 129,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735"
            },
            {
                "name": "Brownie Sundae",
                "description": "Warm brownie served with vanilla ice cream.",
                "price": 199,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1563805042-7684c019e1cb"
            }

        ],

        
                "Biryani House": [

            {
                "name": "Hyderabadi Chicken Biryani",
                "description": "Authentic Hyderabadi dum biryani with tender chicken.",
                "price": 299,
                "vegeterian": False,
                "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1rooZ8KnfY9Yp3C0_H08JukVNbar9Vh6hWpDM9sJCEg&s=10"
            },
            {
                "name": "Mutton Biryani",
                "description": "Fragrant basmati rice with juicy mutton pieces.",
                "price": 369,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1633945274405-b6c8069047b0"
            },
            {
                "name": "Veg Biryani",
                "description": "Basmati rice cooked with fresh vegetables and spices.",
                "price": 229,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1589302168068-964664d93dc0"
            },
            {
                "name": "Paneer Biryani",
                "description": "Spicy paneer dum biryani.",
                "price": 249,
                "vegeterian": True,
                "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrf5t4rIwNbSvR7adukBjkxX7IGJZEhERTlsF0XkNsLg&s=10"
            },
            {
                "name": "Egg Biryani",
                "description": "Biryani served with boiled eggs and spices.",
                "price": 239,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1681546898018-961e2a05c6fa?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGVnZyUyMGJpcml5YW5pfGVufDB8fDB8fHww"
            },
            {
                "name": "Chicken Fried Rice",
                "description": "Indo-Chinese fried rice with chicken.",
                "price": 229,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1512058564366-18510be2db19"
            },
            {
                "name": "Veg Fried Rice",
                "description": "Fried rice tossed with fresh vegetables.",
                "price": 189,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dmVnJTIwZnJpZWQlMjByaWNlfGVufDB8fDB8fHww"
            },
            {
                "name": "Chicken 65",
                "description": "Spicy deep-fried boneless chicken.",
                "price": 269,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1603360946369-dc9bb6258143"
            },
            {
                "name": "Chicken Kabab",
                "description": "Grilled chicken marinated with Indian spices.",
                "price": 289,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1544025162-d76694265947"
            },
            {
                "name": "Paneer Tikka",
                "description": "Grilled paneer cubes with spices.",
                "price": 249,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7"
            },
            {
                "name": "Butter Naan",
                "description": "Fresh tandoor naan brushed with butter.",
                "price": 59,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1559561724-4ea348cd867f?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8YnV0dGVyJTIwbmFhbnxlbnwwfHwwfHx8MA%3D%3D"
            },
            {
                "name": "Garlic Naan",
                "description": "Soft naan topped with garlic butter.",
                "price": 69,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1601050690597-df0568f70950"
            },
            {
                "name": "Raita",
                "description": "Refreshing curd mixed with onions and cucumber.",
                "price": 49,
                "vegeterian": True,
                "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRusY0Km8sRq6nz3oMYZklykvWG4CVtYu8N3wLsHD8Qug&s=10"
            },
            {
                "name": "Gulab Jamun",
                "description": "Soft milk dumplings in sugar syrup.",
                "price": 99,
                "vegeterian": True,
                "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBsCu1E6gHGPDvhio377DzXcLgGxPTAisqPc18PcScMQ&s=10"
            },
            {
                "name": "Sweet Lassi",
                "description": "Traditional chilled sweet lassi.",
                "price": 89,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1623065422902-30a2d299bbe4"
            }

        ],

                "Chinese Wok": [

            {
                "name": "Veg Hakka Noodles",
                "description": "Stir-fried noodles with fresh vegetables and sauces.",
                "price": 189,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1692815153957-fefd061f078d?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2hpY2tlbiUyMGhha2thJTIwbm9kZGxlc3xlbnwwfHwwfHx8MA%3D%3D"
            },
            {
                "name": "Chicken Hakka Noodles",
                "description": "Noodles tossed with chicken and vegetables.",
                "price": 229,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1617093727343-374698b1b08d"
            },
            {
                "name": "Veg Fried Rice",
                "description": "Classic fried rice with vegetables.",
                "price": 179,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1512058564366-18510be2db19"
            },
            {
                "name": "Chicken Fried Rice",
                "description": "Fried rice with chicken and oriental spices.",
                "price": 229,
                "vegeterian": False,
                "picture": "https://plus.unsplash.com/premium_photo-1694141252774-c937d97641da?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Y2hpY2tlbiUyMGZyaWVkJTIwcmljZXxlbnwwfHwwfHx8MA%3D%3D"
            },
            {
                "name": "Veg Manchurian",
                "description": "Crispy vegetable balls in Manchurian sauce.",
                "price": 199,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1585937421612-70a008356fbe"
            },
            {
                "name": "Chicken Manchurian",
                "description": "Juicy chicken tossed in spicy Manchurian sauce.",
                "price": 249,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1603360946369-dc9bb6258143"
            },
            {
                "name": "Paneer Chilli",
                "description": "Paneer cubes cooked with chilli garlic sauce.",
                "price": 239,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7"
            },
            {
                "name": "Chicken Chilli",
                "description": "Boneless chicken tossed with capsicum and onions.",
                "price": 279,
                "vegeterian": False,
                "picture": "https://images.unsplash.com/photo-1544025162-d76694265947"
            },
            {
                "name": "Veg Spring Rolls",
                "description": "Crispy spring rolls stuffed with vegetables.",
                "price": 169,
                "vegeterian": True,
                "picture": "https://plus.unsplash.com/premium_photo-1695756121533-3f60bee7ba7b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dmVnJTIwc3ByaW5nJTIwcm9sbHN8ZW58MHx8MHx8fDA%3D"
            },
            {
                "name": "Chicken Momos",
                "description": "Steamed chicken dumplings served with spicy chutney.",
                "price": 199,
                "vegeterian": False,
                "picture": "https://plus.unsplash.com/premium_photo-1673769108070-580fe90b8de7?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2hpY2tlbiUyMG1vbW9zfGVufDB8fDB8fHww"
            },
            {
                "name": "Veg Momos",
                "description": "Steamed vegetable dumplings.",
                "price": 179,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1694923450868-b432a8ee52aa?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dmVnJTIwbW9tb3N8ZW58MHx8MHx8fDA%3D"
            },
            {
                "name": "Hot & Sour Soup",
                "description": "Spicy and tangy Chinese soup.",
                "price": 129,
                "vegeterian": True,
                "picture": "https://images.unsplash.com/photo-1613844237701-8f3664fc2eff?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aG90JTIwYW5kJTIwc291ciUyMHNvdXB8ZW58MHx8MHx8fDA%3D"
            },
            {
                "name": "Sweet Corn Soup",
                "description": "Creamy sweet corn soup.",
                "price": 119,
                "vegeterian": True,
                "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVUEt896kd1RPXmDCkj7jjXf68AmAa7mS2ybSvFprj9A&s=10"
            },
            {
                "name": "Schezwan Noodles",
                "description": "Spicy noodles cooked with Schezwan sauce.",
                "price": 219,
                "vegeterian": True,
                "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLhOBuNu1G8cZgv7wHSzsXem5SRMc3YSyAq3MwKr5kqA&s=10"
            },
            {
                "name": "Dragon Chicken",
                "description": "Crispy chicken coated in spicy dragon sauce.",
                "price": 299,
                "vegeterian": False,
                "picture": "https://plus.unsplash.com/premium_photo-1669742928112-19364a33b530?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZHJhZ29uJTIwY2hpY2tlbnxlbnwwfHwwfHx8MA%3D%3D"
            }

        ],

        "South Spice": [

    {
        "name": "Masala Dosa",
        "description": "Crispy dosa stuffed with potato masala.",
        "price": 120,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976"
    },
    {
        "name": "Plain Dosa",
        "description": "Traditional crispy South Indian dosa.",
        "price": 90,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1743615467363-250466982515?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGxhaW4lMjBkb3NhfGVufDB8fDB8fHww"
    },
    {
        "name": "Mysore Masala Dosa",
        "description": "Spicy Mysore style dosa with chutney.",
        "price": 140,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1694849789325-914b71ab4075?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bXlzb3JlJTIwbWFzYWxhJTIwZG9zYXxlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "name": "Idli",
        "description": "Soft steamed rice cakes served with chutney.",
        "price": 70,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc"
    },
    {
        "name": "Vada",
        "description": "Crispy medu vada served with sambar.",
        "price": 80,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1728508707623-56d3dca51187?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8dmFkYXxlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "name": "Idli Vada Combo",
        "description": "Two idlis and one medu vada.",
        "price": 110,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDFJdCq9zzvDqq7-n7LTI3e1-XzEB2QcVn2wlg7beJxQ&s"
    },
    {
        "name": "Pongal",
        "description": "Creamy South Indian rice and lentil dish.",
        "price": 120,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtC8nSoXFbBxrfU0QALGa-YhA52K9cH9iML6j945m_AA&s=10"
    },
    {
        "name": "Poori Bhaji",
        "description": "Fluffy pooris with potato curry.",
        "price": 110,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-W_oKTlNual9SmCEcsHyTpprnrfKHWTTFGpBLdJogfQ&s=10"
    },
    {
        "name": "Curd Rice",
        "description": "Refreshing curd rice with tempering.",
        "price": 100,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1633383718081-22ac93e3db65?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3VyZCUyMHJpY2V8ZW58MHx8MHx8fDA%3D"
    },
    {
        "name": "Lemon Rice",
        "description": "Tangy rice with mustard and curry leaves.",
        "price": 110,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQncQGbYLuZnwV-HAmnHGo-ZyME7ic_b7tyL8DB7NW3Ig&s=10"
    },
    {
        "name": "Tomato Rice",
        "description": "Spicy tomato flavored rice.",
        "price": 120,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1665332195309-9d75071138f0?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8VG9tYXRvJTIwcmljZXxlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "name": "Filter Coffee",
        "description": "Authentic South Indian filter coffee.",
        "price": 50,
        "vegeterian": True,
        "picture": "data:image/jpeg;base64,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"
    },
    {
        "name": "Rava Kesari",
        "description": "Traditional semolina sweet.",
        "price": 80,
        "vegeterian": True,
        "picture": "https://plus.unsplash.com/premium_photo-1677955239184-fd35758d3b1c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cmF2YSUyMGtlc3JpfGVufDB8fDB8fHww"
    },
    {
        "name": "Mini Meals",
        "description": "Rice, sambar, rasam, curry and papad.",
        "price": 180,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1680993032090-1ef7ea9b51e5?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8bWluaSUyMGluZGlhbiUyMG1lYWx8ZW58MHx8MHx8fDA%3D"
    },
    {
        "name": "South Indian Meals",
        "description": "Unlimited traditional meals.",
        "price": 250,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe-URJ_4nTY3W-E8WtF8m_zsyOkP4I-IT3Wswr87BGVQ&s=10"
    }
],

"Taco Fiesta": [

    {
        "name": "Veg Taco",
        "description": "Crunchy taco filled with vegetables and cheese.",
        "price": 149,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1552332386-f8dd00dc2f85"
    },
    {
        "name": "Chicken Taco",
        "description": "Grilled chicken taco with salsa.",
        "price": 189,
        "vegeterian": False,
        "picture": "https://images.unsplash.com/photo-1613514785940-daed07799d9b"
    },
    {
        "name": "Paneer Taco",
        "description": "Paneer taco with spicy Mexican sauce.",
        "price": 169,
        "vegeterian": True,
        "picture": "data:image/jpeg;base64,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"
    },
    {
        "name": "Veg Burrito",
        "description": "Mexican burrito with beans and vegetables.",
        "price": 229,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f"
    },
    {
        "name": "Chicken Burrito",
        "description": "Chicken burrito with rice and salsa.",
        "price": 259,
        "vegeterian": False,
        "picture": "data:image/jpeg;base64,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"
    },
    {
        "name": "Nachos",
        "description": "Crunchy nachos with cheese dip.",
        "price": 169,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTo1ZMX1jwi92giURNLkNlLR1kV1WYmLJRmL8YqRw1QcQ&s=10"
    },
    {
        "name": "Loaded Nachos",
        "description": "Nachos topped with beans and cheese.",
        "price": 229,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d"
    },
    {
        "name": "Chicken Quesadilla",
        "description": "Grilled tortilla stuffed with chicken and cheese.",
        "price": 269,
        "vegeterian": False,
        "picture": "https://images.unsplash.com/photo-1618040996337-56904b7850b9"
    },
    {
        "name": "Veg Quesadilla",
        "description": "Cheesy vegetable quesadilla.",
        "price": 239,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEbSKIjAIbkq0A9igO_kv8CBpus_uGzosusEPwICjyUw&s=10"
    },
    {
        "name": "French Fries",
        "description": "Crispy golden fries.",
        "price": 99,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877"
    },
    {
        "name": "Mexican Rice",
        "description": "Rice cooked with Mexican spices.",
        "price": 199,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1512058564366-18510be2db19"
    },
    {
        "name": "Chicken Rice Bowl",
        "description": "Mexican chicken rice bowl.",
        "price": 249,
        "vegeterian": False,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRyMQgZL6TWKFVmrcfMwzf4Ci1tGn4n4Pr6Zz9jpQzPQ&s=10"
    },
    {
        "name": "Churros",
        "description": "Mexican fried dessert with cinnamon.",
        "price": 149,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsHGPi0bmBIJ8EgLpRrnuhQZhCfzSz09x314aL0QBY1Q&s=10"
    },
    {
        "name": "Chocolate Shake",
        "description": "Rich chocolate milkshake.",
        "price": 149,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1572490122747-3968b75cc699"
    },
    {
        "name": "Lemon Soda",
        "description": "Refreshing lemon soda.",
        "price": 79,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd"
    }

],

"BBQ Nation": [

    {
        "name": "Chicken BBQ Wings",
        "description": "Smoky grilled chicken wings.",
        "price": 299,
        "vegeterian": False,
        "picture": "https://images.unsplash.com/photo-1527477396000-e27163b481c2"
    },
    {
        "name": "Chicken Tikka",
        "description": "Tender grilled chicken with Indian spices.",
        "price": 329,
        "vegeterian": False,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT56AlKha3Cmo3ukFpf64H9c0ObNCSiPMt-8jDxm639Q&s=10"
    },
    {
        "name": "Paneer Tikka",
        "description": "Grilled paneer cubes with spices.",
        "price": 269,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7"
    },
    {
        "name": "Fish Tikka",
        "description": "Fresh fish grilled to perfection.",
        "price": 349,
        "vegeterian": False,
        "picture": "https://images.unsplash.com/photo-1559847844-5315695dadae"
    },
    {
        "name": "Veg Seekh Kebab",
        "description": "Mixed vegetable seekh kebab.",
        "price": 229,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeAew7NlTxo0t32yD80n8BHr34CgB0XYLRjcvX1dAXnQ&s=10"
    },
    {
        "name": "Chicken Seekh Kebab",
        "description": "Juicy chicken seekh kebab.",
        "price": 299,
        "vegeterian": False,
        "picture": "https://images.unsplash.com/photo-1544025162-d76694265947"
    },
    {
        "name": "Mutton Seekh Kebab",
        "description": "Grilled mutton seekh kebab.",
        "price": 349,
        "vegeterian": False,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7QSTRc-cACDLL6IOiKIMXpTZBpaaXB6DTpSmHzYnxSA&s=10"
    },
    {
        "name": "Butter Chicken",
        "description": "Creamy butter chicken curry.",
        "price": 329,
        "vegeterian": False,
        "picture": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398"
    },
    {
        "name": "Veg Biryani",
        "description": "Aromatic biryani with vegetables.",
        "price": 229,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvVqxfmsUlXci4Gq_0qCR1iZgxxRKitcH5m_9uj7LPlw&s=10"
    },
    {
        "name": "Chicken Biryani",
        "description": "Fragrant chicken dum biryani.",
        "price": 299,
        "vegeterian": False,
        "picture": "https://images.unsplash.com/photo-1589302168068-964664d93dc0"
    },
    {
        "name": "Garlic Naan",
        "description": "Fresh garlic naan.",
        "price": 69,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDsU671RUysGC9j64yXmj_dryoGPWLyxAQzYyejQ_vpw&s=10"
    },
    {
        "name": "Brownie with Ice Cream",
        "description": "Warm brownie served with vanilla ice cream.",
        "price": 179,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1563805042-7684c019e1cb"
    },
    {
        "name": "Gulab Jamun",
        "description": "Soft gulab jamun in sugar syrup.",
        "price": 99,
        "vegeterian": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBsCu1E6gHGPDvhio377DzXcLgGxPTAisqPc18PcScMQ&s=10"
    },
    {
        "name": "Mango Lassi",
        "description": "Refreshing mango yogurt drink.",
        "price": 99,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1623065422902-30a2d299bbe4"
    },
    {
        "name": "Soft Drink",
        "description": "Chilled soft drink.",
        "price": 60,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1554866585-cd94860890b7"
    }

]

    }
    for restaurant_name, menu in restaurants.items():

        restaurant, created = Restaurant.objects.update_or_create(
            name=restaurant_name,
            defaults={
                "picture": "https://picsum.photos/600/400",
                "cuisine": "Multi Cuisine",
                "rating": 4.5
            }
        )

        for item in menu:
            Item.objects.update_or_create(
                restaurant=restaurant,
                name=item["name"],
                defaults={
                    "description": item["description"],
                    "price": item["price"],
                    "vegeterian": item["vegeterian"],
                    "picture": item["picture"]
                }
            )

    print("✅ Data inserted successfully!")