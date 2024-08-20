// src/App.tsx
import React, { useState } from "react";
import Hello from "./Hello";
import ListGroup from "./components/ListGroup";
import Alert from "./components/Alert";
import Button from "./components/Button";

const App: React.FC = () => {
  let city_items = ["New York", "San Francisco", "Tokyo", "London", "Paris"];
  // let cat_items = ["Maine Coon", "Ragdoll", "Persian", "Abyssinian", "Siamese"];

  const [alertVisible, setAlertVisible] = useState(false);

  const handleSelectItem = (heading: string, item: string) => {
    console.log(`Heading: ${heading}, Item: ${item}`);
  };

  const onClick = () => {
    console.log("Button have been clicked!");
    setAlertVisible(true);
  };

  return (
    <div>
      <Hello name="World" />
      <ListGroup
        items={city_items}
        heading="Cities"
        onSelectItem={handleSelectItem}
      ></ListGroup>
      {alertVisible && (
        <Alert>
          Hello <span>World</span>
        </Alert>
      )}
      <Button color="primary" onClick={onClick}>
        This is a Button
      </Button>
      {/* <ListGroup
        items={cat_items}
        heading="Cats"
        onSelectItem={handleSelectItem}
      ></ListGroup> */}
    </div>
  );
};

export default App;
