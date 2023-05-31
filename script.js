var products = [
    {
        id: 1,
        name: "Mountain Bike Rockrider ST20 Low Frame - Blue",
        description: "Designed for leisure cycling on off-road trails and urban conditions. Easy to adjust the seat height and remove the front wheel with a quick-release. Lifetime warranty on the frame & fork and 2 years warranty on non-wearing parts.",
        price: 10000,
        image:"./cyclefinal"

    },
    {
        id: 2,
        name: "Audio-Technica - ATH-M50x",
        description: "Designed in Japan. Flat sound signature. 3 years of warranty. Aesthetic and ergonomic design. Ideal for audiophiles. For professionals. 45mm Dynamic Drivers. Replaceable Cables.",
        price: 11500,
        image:"./HEADPHONE2.png"
    },
    {
        id: 3,
        name: "iPhone 14",
        description: "Emergency SOS Crash Detection. Pro camera system. 48MP Main | Ultra Wide Telephoto Photonic Engine for incredible detail and color Autofocus on TrueDepth front camera. Up to 29 hours video playback footnote.",
        price: 80000,
        image:"./PHONE2.jpg"
    },
    {
        id: 4,
        name: "HP Envy X360 Ryzen 5",
        description: "AMD Ryzen™ 5 processor. Windows 11 Home. 33.8 cm (13.3) diagonal FHD touch display. 16 GB DDR4-3200 MHz RAM (onboard). 512 GB PCIe® NVMe™ M.2 SSD. Limitless creation, from anywhere. AMD Radeon™ Graphics. 1 SuperSpeed USB Type-C® 10Gbps signaling rate (USB Power Delivery, DisplayPort™ 1.4, HP Sleep and Charge); 1 SuperSpeed USB Type-A 5Gbps signaling rate (HP Sleep and Charge); 1 SuperSpeed USB Type-A 5Gbps signaling rate; 1 AC smart pin; 1 headphone/microphone combo. Up to 15 hours and 30 minutes. 1 year (1/1/0) limited warranty.",
        price: 65000,
        image:"./LAPTOP2.jpg"
    },
    {
        id: 5,
        name: "Smart Bottle",
        description: "Track your daily water intake seamlessly with Tap to Track Bottle, which integrates with the HealthifyMe app to make hydration tracking effortless. Tap your mobile device's NFC sensor on the tag of the Tap To Track bottle to initiate the tracking process.",
        price: 800,
        image:"./Bottle.webp"
    },
    {
        id: 6,
        name: "Multifunction Waterproof Laptop Travel Backpack",
        description: "Wrinkle-free bag and 3x more water-resistant with Rainproof zippers. Trolley sleeve to securely place the bags on the luggage. Capacity: 36-55 Litre. Convenient for Flight Cabin Luggage. Right-sized with sturdy stitching. Dimension: (43cmx30cmx20cm). Color - Blue. Padded laptop compartment fits up to 15 Laptop. Back padding with Air mesh.",
        price: 1000,
        image:"./BAGFINAL.jpg"
    },
    {
        id: 7,
        name: "Havells Altro 1.5Ltr Kettle Stainless Steel",
        description: "APP.ELE.36593721. Capacity: 1.5 Litre. Color: Black. Material: Stainless Steel; Plastic. Voltage: 230 V. Type of Product: Electric Kettle. Model No: GHBKTAYK125. Power: 1250W.",
        price: 10000,
        image:"./kettlefinal"
    },
    {
        id: 8,
        name: "Samsung Q60B QLED 4K Smart TV",
        description: "Quantum HDR. Sleek and slim, more than ever. AirSlim. 1m 38cm 55. Samsung's new Smart Hub puts content curation and discovery front and center, so you spend less time searching and more time streaming movies, shows, and other contents you enjoy.",
        price: 70000,
        image:"./tvfinal"
    },
    {
        id: 9,
        name: "LG RS-Q19APYE 2023 Model",
        description: "White 1.5 Ton 4 Star Inverter Split AC. Capacity: 1.5 Ton. Suitable for medium-sized rooms (111 to 150 sq ft.). 653/1236 (In/Out) CFM Air Circulation & Ambient Temperature: 52 degrees Celsius with 4-way air swing. Energy Rating: 4 Star - High energy efficiency. Annual Energy Consumption: 838.50 Units Per Year.",
        price: 90000,
        image:"./ACFINAL.jpg"

    },
    {
        id: 10,
        name: "Hamilton Beach Professional Juicer Mixer Grinder",
        description: "58770-IN, 1400 Watt Rated Motor, Triple Overload Protection, 3 Stainless Steel Leakproof Jars, Triple Safety Protection, Intelligent Controls, Black",
        price: 23999,
        image:"./Mixer.jpg"
    }
];

var cartItems = [];

function openModal(productId) {
    var modal = document.getElementById("modal");
    var product = products.find(function(item) {
        return item.id === productId;
    });

    if (product) {
        document.getElementById("product-title").textContent = product.name;
        document.getElementById("product-description").textContent = product.description;
        modal.style.display = "block";
    }
}

function closeModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
}

function addToCart(productId) {
    var product = products.find(function(item) {
        return item.id === productId;
    });

    if (product) {
        cartItems.push({ name: product.name, price: product.price,image:product.image });
        displayCartItems();
    }
}
function removeCartItem(index) {
    cartItems.splice(index, 1);
    displayCartItems();
  }
  
  function clearCart() {
    cartItems = [];
    displayCartItems();
  }

function displayCartItems() {
    var cartList = document.getElementById("cart-items");
    cartList.innerHTML = "";

    var totalPrice = 0;

    cartItems.forEach(function(item, index) {
        var li = document.createElement("li");
        var img = document.createElement("img");
        var removeBtn = document.createElement("button");

        img.src = item.image;
        img.classList.add("cart_img")

        li.textContent = item.name + " - Rs " + item.price;

        removeBtn.textContent = "Remove";
        removeBtn.classList.add("remove-btn");
        removeBtn.addEventListener("click", function() {
          removeCartItem(index);
    }); 
        cartList.appendChild(img);
        cartList.appendChild(li);
        cartList.appendChild(removeBtn);

        totalPrice += item.price;
    });

    var totalElement = document.getElementById("total-price");
    totalElement.textContent = "Total: Rs " + totalPrice;
}
function redirectToCheckout() {
    window.location.href = "checkout.html";
}