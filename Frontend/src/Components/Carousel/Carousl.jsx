import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";
import Card from "../Cards/Card";

export default function Carousl({ movies }) {
  const responsive = {
    largescreens: {
      breakpoint: { max: 3000, min: 2400 },
      items: 6,
      slidesToSlide: 5, // optional, default to 1.
    },
    desktop: {
      breakpoint: { max: 2400, min: 1500 },
      items: 5,
      slidesToSlide: 5,
    },
    tablet: {
      breakpoint: { max: 1500, min: 1200 },
      items: 4,
      slidesToSlide: 3,
    },
    phones: {
      breakpoint: { max: 1200, min: 900 },
      items: 3,
      slidesToSlide: 2,
    },
    mobile: {
      breakpoint: { max: 900, min: 630 },
      items: 2,
      slidesToSlide: 1,
    },
    smaller_mobile: {
      breakpoint: { max: 630, min: 0 },
      items: 1,
      slidesToSlide: 1,
    },
  };

  const cardies = movies.map((item) => <Card key={item.title} {...item} />);
  return (
    <div>
      <Carousel responsive={responsive}>{cardies}</Carousel>
    </div>
  );
}
