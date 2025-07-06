import { useState } from "react";

const ContactForm = ({}) => {
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [email, setEmail] = useState("");

  const onSubmit = async (e) => {
    e.preventDefault();
    const data = { first_name, last_name, email };
    const url = "http://127.0.0.1:5000/create_contact";
    const option = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };
    const response = await fetch(url, option);
    if (response.status !== 201 && response.status !== 200) {
      const data = await response.json();
      alert(data.message);
    } else {
      console.log(data);
      //Success
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label>First Name:</label>
        <input
          id="firstName"
          type="text"
          value={first_name}
          onChange={(e) => setFirstName(e.target.value)}
        />
      </div>
      <div>
        <label>Last Name:</label>
        <input
          id="lastName"
          type="text"
          value={last_name}
          onChange={(e) => setLastName(e.target.value)}
        />
      </div>
      <div>
        <label>Email:</label>
        <input
          id="email"
          type="text"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <button type="submit"> Create Contact</button>
    </form>
  );
};

export default ContactForm;
