# Define FAQs and their responses
import tkinter as tk
from tkinter import scrolledtext, font
from PIL import Image, ImageTk

faqs = {
    "order tracking": {
        "question": ["track my order", "where is my order", "order status", "shipment update"],
        "response": "You can track your order by logging into your account and visiting the 'Order History' section. "
                    "If you haven't received a tracking number, check your email or contact support."
    },
    "refund": {
        "question": ["get a refund", "return my order", "refund policy", "money back"],
        "response": "To request a refund, please visit our 'Returns' section and follow the instructions. "
                    "Most refunds are processed within 5-7 business days after we receive your item. "
                    "If you experience any issues, reach out to our customer service team."
    },
    "delivery time": {
        "question": ["how long does delivery take", "delivery time", "when will my order arrive", "shipping duration"],
        "response": "Standard delivery takes 3-5 business days. Express delivery is available for an additional fee "
                    "and usually arrives within 1-2 days. International shipping times vary depending on the destination."
    },
    "contact support": {
        "question": ["contact support", "customer service contact", "support email", "help desk"],
        "response": "You can reach our support team at support@ecommerce.com or call +123-456-7890. "
                    "Our team is available Monday to Friday, from 9 AM to 6 PM."
    },
    "payment methods": {
        "question": ["payment methods", "how can I pay", "accepted payments", "available payment options"],
        "response": "We accept Visa, MasterCard, PayPal, Apple Pay, and bank transfers. "
                    "Cryptocurrency payments are not yet supported, but we are working on adding more options soon!"
    },
    "change order": {
        "question": ["change my order", "modify order", "edit order", "update order details"],
        "response": "Once an order is placed, it cannot be modified. However, you may cancel and reorder if needed. "
                    "For urgent changes, please contact our support team as soon as possible."
    },
    "cancel order": {
        "question": ["cancel my order", "how to cancel order", "stop my order", "order cancellation"],
        "response": "To cancel an order, go to your 'Order History' and select the cancellation option. "
                    "Orders can only be canceled before they are shipped. If your order has already been dispatched, "
                    "you can initiate a return once you receive it."
    },
    "lost package": {
        "question": ["lost package", "did not receive order", "missing order", "package not delivered"],
        "response": "If your package is missing, please track it using the tracking link sent via email. "
                    "If it's marked as delivered but not received, check with neighbors or your local post office. "
                    "If you still can't locate it, contact us for further assistance."
    },
    "international shipping": {
        "question": ["international shipping", "ship outside country", "overseas delivery", "shipping abroad"],
        "response": "Yes, we offer international shipping to most countries. "
                    "Shipping fees and delivery times vary based on your location. "
                    "Please check our 'Shipping Policy' page for more details."
    },
    "discounts and coupons": {
        "question": ["discounts", "coupon codes", "promo code", "available deals"],
        "response": "You can find available promo codes on our website's 'Deals' section. "
                    "Sign up for our newsletter to receive exclusive discounts!"
    },
    "return policy": {
        "question": ["return policy", "return conditions", "how to return", "return process"],
        "response": "Items can be returned within 30 days of purchase, provided they are unused and in original packaging. "
                    "To initiate a return, visit our 'Returns' section and follow the instructions."
    },
    "security and privacy": {
        "question": ["security", "privacy policy", "data protection", "customer data safety"],
        "response": "We prioritize customer privacy and use encrypted transactions to protect your data. "
                    "Read our full policy in the 'Privacy' section of our website."
    },
    "sell on platform": {
        "question": ["sell on your website", "become a seller", "merchant account", "vendor registration"],
        "response": "Interested in selling with us? Visit our 'Sell with Us' page for registration details. "
                    "We offer support for new merchants to help them get started."
    },
    "membership benefits": {
        "question": ["membership program", "VIP benefits", "loyalty rewards", "exclusive perks"],
        "response": "Join our membership program to enjoy exclusive discounts, early access to sales, and reward points. "
                    "Check the 'Membership' section for more details."
    },
    "gift wrapping": {
        "question": ["gift wrap", "gift packaging", "wrapped present", "special gift"],
        "response": "We offer gift wrapping services for a small fee. "
                    "You can select this option at checkout and even include a personalized message."
    },
    "size guide": {
        "question": ["size chart", "fit guide", "which size to buy", "sizing help"],
        "response": "Check our size guide available on each product page. "
                    "If you need further assistance, contact our support team."
    },
    "damaged item": {
        "question": ["damaged item", "broken product", "defective order", "faulty goods"],
        "response": "We apologize if you received a damaged product. "
                    "Please contact us with photos of the item, and we will arrange a replacement or refund."
    },
    "order confirmation": {
        "question": ["order confirmation", "did my order go through", "payment confirmation", "order received"],
        "response": "After placing an order, you should receive a confirmation email within a few minutes. "
                    "If you haven't received it, check your spam folder or contact support."
    },
    "store locations": {
        "question": ["store locations", "physical store", "where to buy in person", "visit a store"],
        "response": "We currently operate online only, but we are planning to open physical stores soon!"
    }
}




class ECommerceChatbot:
    def __init__(self):
        self.context = None  # To store context for follow-up questions

    def match_faq(self, user_input):
        """Match user input to the most relevant FAQ."""
        user_input = user_input.lower()  # Convert input to lowercase for better matching

        best_match = None
        max_score = 0

        # Find the best matching FAQ
        for key, value in faqs.items():
            for question in value["question"]:
                score = sum(1 for word in question.split() if word in user_input)
                if score > max_score:
                    max_score = score
                    best_match = key

        return faqs[best_match]["response"] if best_match else "I'm sorry, I couldn't find an answer to your question. Please contact support."

class ChatbotGUI:
    def __init__(self, root):
        self.bot = ECommerceChatbot()
        
        root.title("E-Commerce Chatbot")
        root.geometry("619x757")  # Taller and narrower window
        root.configure(bg="#f0f0f0")  # Light gray background

        # Load logos
        self.user_logo = Image.open("user.png")  # Replace with your user logo file
        self.user_logo = self.user_logo.resize((30, 30))  # Resize user logo
        self.user_logo = ImageTk.PhotoImage(self.user_logo)

        self.bot_logo = Image.open("robot.png")  # Replace with your bot logo file
        self.bot_logo = self.bot_logo.resize((30, 30))  # Resize bot logo
        self.bot_logo = ImageTk.PhotoImage(self.bot_logo)

        # Load the send icon
        self.send_icon = Image.open("send_icon.png")  # Replace with your send icon file
        self.send_icon = self.send_icon.resize((30, 30))  # Resize send icon
        self.send_icon = ImageTk.PhotoImage(self.send_icon)

        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=30, state=tk.DISABLED, bg="#ffffff", bd=0, font=("Arial", 10))
        self.chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Input frame for user input and send button
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=5, padx=10, fill=tk.X)

        # User input field
        self.user_input = tk.Entry(input_frame, width=30, bg="#ffffff", bd=0, font=("Arial", 10))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Send button with icon
        self.send_button = tk.Button(input_frame, image=self.send_icon, command=self.get_response, bd=0, bg="#f0f0f0")
        self.send_button.pack(side=tk.RIGHT, padx=(5, 0))

        # Bind Enter key to send message
        root.bind("<Return>", self.get_response)

    def get_response(self, event=None):
        """Handle user input and chatbot response."""
        user_message = self.user_input.get().strip()
        if user_message:
            self.display_message(user_message, is_user=True)
            response = self.bot.match_faq(user_message)
            self.display_message(response, is_user=False)
            self.user_input.delete(0, tk.END)

    def display_message(self, message, is_user):
        """Display messages in the chat window with logos and chat bubbles."""
        self.chat_display.config(state=tk.NORMAL)
        
        # Create a frame for the message bubble
        frame = tk.Frame(self.chat_display, bg="#f0f0f0", bd=0)
        frame.pack(pady=5, padx=10, anchor=tk.E if is_user else tk.W)

        # Add user or bot logo
        if is_user:
            logo_label = tk.Label(frame, image=self.user_logo, bg="#f0f0f0")
            logo_label.pack(side=tk.RIGHT, padx=(5, 0))
        else:
            logo_label = tk.Label(frame, image=self.bot_logo, bg="#f0f0f0")
            logo_label.pack(side=tk.LEFT, padx=(0, 5))

        # Create the message bubble
        bubble = tk.Label(frame, text=message, bg="#0078d7" if is_user else "#ffffff", fg="#ffffff" if is_user else "#000000", 
                          bd=0, padx=10, pady=5, font=("Arial", 10), wraplength=300, justify=tk.LEFT)
        bubble.pack(side=tk.RIGHT if is_user else tk.LEFT)

        # Add the bubble to the chat display
        self.chat_display.window_create(tk.END, window=frame)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.yview(tk.END)

# Run the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()