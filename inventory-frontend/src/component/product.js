
import Wrapper from "./wrapper"
import {useEffect, useState} from "react";
import {Link} from "react-router-dom";

function Product(){

    const [products, setProudcts] = useState([])

    useEffect( ()=>{
        fetchProducts()
    },[])

    const fetchProducts = async () =>{
        const response = await fetch('http://localhost:8000/products')
        if (!response.ok) {
            throw new Error('Network response was not ok')
        }
        const productList = await response.json()
        setProudcts(productList)
    }

    const del = async (id) => {
        console.log(id)
    }

    return(
        <div>
             <Wrapper>
                <div className="pt-3 pb-2 mb-3 border-bottom">
                    <Link to={`/create`} className="btn btn-sm btn-outline-secondary">Add</Link>
                </div>

                <div className="table-responsive">
                    <table className="table table-striped table-sm">
                        <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Name</th>
                            <th scope="col">Price</th>
                            <th scope="col">Quantity</th>
                            <th scope="col">Actions</th>
                        </tr>
                        </thead>
                        <tbody>
                        {products.map(product => {
                            return <tr key={product.id}>
                                <td>{product.id}</td>
                                <td>{product.name}</td>
                                <td>{product.price}</td>
                                <td>{product.quantity}</td>
                                <td>
                                    <a href="#" className="btn btn-sm btn-outline-secondary"
                                    onClick={e => del(product.id)}
                                    >
                                        Delete
                                    </a>
                                </td>
                            </tr>
                        })}
                        </tbody>
                    </table>
                </div>
             </Wrapper>
        </div>
    )
}

export default Product