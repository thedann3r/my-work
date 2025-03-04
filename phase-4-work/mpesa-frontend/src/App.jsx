import React, { useState } from "react";
import axios from "axios";
import "./mpesa.css"; 

function App() {
  const [phone, setPhone] = useState("254");
  const [amount, setAmount] = useState("");
  const [loading, setLoading] = useState(false);

  // Handle phone number input with validation
  const handlePhoneChange = (e) => {
    let input = e.target.value;

    // Ensure "254" is always there and restrict to 9 more digits
    if (!input.startsWith("254")) {
      input = "254";
    } else if (input.length > 12) {
      input = input.slice(0, 12); // Max length 12 (254 + 9 digits)
    }

    setPhone(input);
  };

  const handlePay = (e) => {
    e.preventDefault();

    if (!phone || phone.length !== 12 || !amount) {
      alert("Please enter a valid phone number and amount.");
      return;
    }

    setLoading(true);

    axios
      .post(
        "http://127.0.0.1:5000/mpesa/pay",
        { phone_number: phone, amount: amount },
        { headers: { "Content-Type": "application/json", "Accept": "application/json" } }
      )
      .then((response) => {
        console.log("Payment Response:", response.data);
        alert("Payment successful! Check your phone for confirmation.");
      })
      .catch((error) => {
        console.error("Payment Error:", error);
        if (error.response) {
          alert(`Error: ${error.response.data.error || "Payment failed!"}`);
        } else {
          alert("Payment failed! Please try again.");
        }
      })
      .finally(() => {
        setLoading(false);
      });
  };

  return (
    <div className="container">
      <h2 className="title">Marksmatt</h2>
      <p className="subtitle">
        Pay with <span className="mpesa-text">M<span className="hyphen">-</span>pesa</span>
      </p>

      <form className="payment-form" onSubmit={handlePay}>
        {/* Phone Number Input (Auto-fills "254") */}
        <input
          type="text"
          value={phone}
          onChange={handlePhoneChange}
          className="input-field"
          placeholder="2547XXXXXXXX"
          required
        />

        {/* Amount Input */}
        <input
          type="number"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          className="input-field"
          placeholder="Enter amount"
          required
        />

        {/* Pay Button */}
        <button type="submit" className="pay-button" disabled={loading}>
          {loading ? "Processing..." : "Pay Now"}
        </button>
      </form>
    </div>
  );
}

export default App;
