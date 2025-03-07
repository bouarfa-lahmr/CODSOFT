import random
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only required once)
nltk.download("punkt")

# Define FAQs and their responses
faqs = {
    "order tracking": {
        "question": ["how can i track my order?", "where is my order?", "order status"],
        "response": "You can track your order by logging into your account and visiting the 'Order History' section. Your order status will be displayed there."
    },
    "refund": {
        "question": ["how do i get a refund?", "can i return my order?", "refund policy"],
        "response": "To request a refund, please contact our support team at support@ecommerce.com with your order number. Our refund policy allows returns within 30 days of delivery."
    },
    "business hours": {
        "question": ["what are your business hours?", "when are you open?", "customer service hours"],
        "response": "Our customer service is available from 9 AM to 6 PM, Monday to Friday."
    },
    "delivery time": {
        "question": ["how long does delivery take?", "delivery time", "when will my order arrive?"],
        "response": "Standard delivery takes 3-5 business days. Express delivery is available for an additional fee."
    },
    "contact support": {
        "question": ["how can i contact support?", "customer service contact", "support email"],
        "response": "You can reach our support team at support@ecommerce.com or call us at +123-456-7890."
    },
    "payment methods": {
        "question": ["what payment methods do you accept?", "can i pay with credit card?", "do you accept paypal?"],
        "response": "We accept all major credit cards (Visa, MasterCard, American Express), PayPal, and bank transfers."
    },
    "product availability": {
        "question": ["is this product in stock?", "when will this item be back in stock?", "product availability"],
        "response": "You can check the availability of a product on its product page. If it's out of stock, you can sign up for notifications when it's back in stock."
    },
    "shipping costs": {
        "question": ["how much is shipping?", "do you offer free shipping?", "shipping fees"],
        "response": "Standard shipping costs $5.99. Free shipping is available for orders over $50."
    },
    "cancel order": {
        "question": ["how can i cancel my order?", "can i cancel my order after placing it?", "order cancellation"],
        "response": "You can cancel your order within 24 hours of placing it. Please contact our support team at support@ecommerce.com with your order number."
    },
    "change order": {
        "question": ["can i change my order?", "modify order", "change shipping address"],
        "response": "You can modify your order within 1 hour of placing it. After that, please contact our support team for assistance."
    },
    "return policy": {
        "question": ["what is your return policy?", "can i return a product?", "return conditions"],
        "response": "You can return products within 30 days of delivery, provided they are unused and in their original packaging. Please contact support for a return label."
    },
    "discounts": {
        "question": ["do you offer discounts?", "promo codes", "coupons"],
        "response": "We regularly offer discounts and promo codes. Check our website or subscribe to our newsletter for the latest deals."
    },
    "account issues": {
        "question": ["i can't log in to my account", "account login issues", "forgot password"],
        "response": "If you're having trouble logging in, use the 'Forgot Password' feature to reset your password. If the issue persists, contact support."
    },
    "international shipping": {
        "question": ["do you ship internationally?", "international delivery", "shipping to other countries"],
        "response": "Yes, we ship internationally. Shipping costs and delivery times vary by country. Please check the product page for details."
    },
    "warranty": {
        "question": ["does this product come with a warranty?", "product warranty", "warranty policy"],
        "response": "Most products come with a 1-year manufacturer's warranty. Please check the product description for warranty details."
    },
    "gift cards": {
        "question": ["do you sell gift cards?", "can i buy a gift card?", "gift card balance"],
        "response": "Yes, we offer gift cards in various denominations. You can purchase them on our website or check your gift card balance in your account."
    },
    "size guide": {
        "question": ["where can i find the size guide?", "size chart", "what size should i order?"],
        "response": "You can find the size guide on the product page. If you need further assistance, contact our support team."
    },
    "privacy policy": {
        "question": ["what is your privacy policy?", "how do you use my data?", "data protection"],
        "response": "We take your privacy seriously. You can read our full privacy policy on our website under the 'Privacy Policy' section."
    },
    "terms and conditions": {
        "question": ["where can i find the terms and conditions?", "terms of service", "legal information"],
        "response": "You can find our terms and conditions on our website under the 'Terms and Conditions' section."
    }
}

# Define a class for the chatbot
class ECommerceChatbot:
    def __init__(self):
        self.context = None  # To store context for follow-up questions

    def preprocess_input(self, user_input):
        """Preprocess user input by tokenizing and converting to lowercase."""
        tokens = nltk.word_tokenize(user_input.lower())
        return tokens

    def match_faq(self, user_input):
        """Match user input to the most relevant FAQ."""
        tokens = self.preprocess_input(user_input)
        best_match = None
        max_score = 0

        # Check for the best matching FAQ
        for key, value in faqs.items():
            for question in value["question"]:
                question_tokens = self.preprocess_input(question)
                score = len(set(tokens).intersection(question_tokens))
                if score > max_score:
                    max_score = score
                    best_match = key

        return best_match

    def get_response(self, user_input):
        """Generate a response based on user input and context."""
        if self.context:
            # Handle follow-up questions in the same context
            response = faqs[self.context]["response"]
            self.context = None  # Reset context after responding
            return response

        # Match user input to an FAQ
        matched_faq = self.match_faq(user_input)
        if matched_faq:
            self.context = matched_faq  # Set context for follow-up questions
            return faqs[matched_faq]["response"]
        else:
            return "I'm sorry, I don't understand your question. Please contact our support team for further assistance."

# Main function to run the chatbot
def main():
    chatbot = ECommerceChatbot()
    print("Welcome to the E-commerce FAQ Chatbot! How can I assist you today?")
    print("You can ask about order tracking, refunds, business hours, delivery time, payment methods, and more.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit the chatbot if the user types 'exit'
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for using our FAQ chatbot. Have a great day!")
            break

        # Get the chatbot's response
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()
