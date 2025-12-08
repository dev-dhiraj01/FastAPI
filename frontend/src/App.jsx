import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  // States for Add Product
  const [newProduct, setNewProduct] = useState({
    id: "",
    name: "",
    desc: "",
    price: "",
    quant: "",
  });

  // State for Update Product
  const [editProduct, setEditProduct] = useState(null);

  // Fetch products from FastAPI
  const fetchProducts = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/products");
      const data = await response.json();
      setProducts(data);
    } catch (error) {
      console.error("Error fetching products:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  // Add Product
  const addProduct = async () => {
    await fetch("http://127.0.0.1:8000/products", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newProduct),
    });

    fetchProducts();

    setNewProduct({ name: "", desc: "", price: "", quant: "" });
  };

  // Delete Product
  const deleteProduct = async (id) => {
    await fetch(`http://127.0.0.1:8000/products/${id}`, {
      method: "DELETE",
    });

    
    fetchProducts();
  };

  // Update Product
  const updateProduct = async () => {
    await fetch(`http://127.0.0.1:8000/products/${editProduct.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(editProduct),
    });

    
    setEditProduct(null);
    fetchProducts();
  };

  return (
    <div className="App">
      <h1>Products List</h1>

      {/* Add Product Form */}
      <h2>Add Product</h2>
      <input
        type="number"
        placeholder="ID"
        value={newProduct.id || ""}
        onChange={(e) => setNewProduct({ ...newProduct, id: e.target.value })}
      />
      <input
        type="text"
        placeholder="Name"
        value={newProduct.name || ""}
        onChange={(e) => setNewProduct({ ...newProduct, name: e.target.value })}
      />
      <input
        type="text"
        placeholder="Description"
        value={newProduct.desc || ""}
        onChange={(e) => setNewProduct({ ...newProduct, desc: e.target.value })}
      />
      <input
        type="number"
        placeholder="Price"
        value={newProduct.price || ""}
        onChange={(e) => setNewProduct({ ...newProduct, price: e.target.value })}
      />
      <input
        type="number"
        placeholder="Quantity"
        value={newProduct.quant || ""}
        onChange={(e) => setNewProduct({ ...newProduct, quant: e.target.value })}
      />
      <button onClick={addProduct}>Add Product</button>

      <br />
      <br />

      {loading ? (
        <p>Loading...</p>
      ) : (
        <table border="1" cellPadding="10">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Description</th>
              <th>Price (₹)</th>
              <th>Quantity</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {products.map((item) => (
              <tr key={item.id}>
                <td>{item.id}</td>
                <td>{item.name}</td>
                <td>{item.desc}</td>
                <td>{item.price}</td>
                <td>{item.quant}</td>

                <td>
                  <button onClick={() => setEditProduct(item)}>
                    Update
                  </button>{" "}
                  <button
                    style={{ color: "red" }}
                    onClick={() => deleteProduct(item.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* Update Product Form */}
      {editProduct && (
        <div>
          <h2>Update Product</h2>
          <input
            type="text"
            value={editProduct.name}
            onChange={(e) =>
              setEditProduct({ ...editProduct, name: e.target.value })
            }
          />
          <input
            type="text"
            value={editProduct.desc}
            onChange={(e) =>
              setEditProduct({ ...editProduct, desc: e.target.value })
            }
          />
          <input
            type="number"
            value={editProduct.price}
            onChange={(e) =>
              setEditProduct({ ...editProduct, price: e.target.value })
            }
          />
          <input
            type="number"
            value={editProduct.quant}
            onChange={(e) =>
              setEditProduct({ ...editProduct, quant: e.target.value })
            }
          />

          <button onClick={updateProduct}>Save Changes</button>
          <button onClick={() => setEditProduct(null)}>Cancel</button>
        </div>
      )}
    </div>
  );
}

export default App;
