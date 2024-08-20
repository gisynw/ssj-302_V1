import React, { MouseEvent, useState } from "react";

interface ListGroupProps {
  items: string[];
  heading: string;
  // (item : string) => void
  onSelectItem: (heading: string, item: string) => void;
}

function ListGroup({ items, heading, onSelectItem }: ListGroupProps) {
  // Hook
  const [selectedIndex, setSelectedIndex] = useState(-1);

  const getMessage = () => {
    return items.length === 0 && <p>No item found.</p>;
  };

  return (
    <React.Fragment>
      <h1>{heading}</h1>
      {getMessage()}
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            key={index}
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            // onClick={() => console.log(item + "been clicked\n" + index)}
            onClick={() => {
              setSelectedIndex(index);
              onSelectItem(heading, item);
            }}
          >
            {item}
          </li>
        ))}
      </ul>
    </React.Fragment>
  );
}

export default ListGroup;
