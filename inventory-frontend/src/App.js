
import Product from './component/product';
import ProductCreate from './component/productCreate';
import Order from './component/order';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Product />} />
        <Route path="/create" element={<ProductCreate/>}/>
        <Route path='/order' element={<Order />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
