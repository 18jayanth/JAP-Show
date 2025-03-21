import Recommend_Movies from "./Components/Recommended_Movies/Recommend_Movies";
import Navbar_Carousel from "./Components/Navbar+Carousel/Navbar_Carousel";

import "./App.css";

export default function App() {
  return (
    <div>
      <Navbar_Carousel />
      <Recommend_Movies />
    </div>
  );
}