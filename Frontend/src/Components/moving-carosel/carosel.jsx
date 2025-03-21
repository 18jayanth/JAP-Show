import 'react-multi-carousel/lib/styles.css';
import a from '../../assets/first-caorosel.avif'
import b from '../../assets/second-caorosel.avif'
import c from '../../assets/third-caorosel.avif'
import d from '../../assets/fourth-caorosel.avif'
import Carousel from 'react-multi-carousel';
export default function Moving()
{
    const responsive = {
        superLargeDesktop: {
          // the naming can be any, depends on you.
          breakpoint: { max: 4000, min: 3000 },
          items: 5
        },
        desktop: {
          breakpoint: { max: 3000, min: 1024 },
          items: 1
        },
        tablet: {
          breakpoint: { max: 1024, min: 464 },
          items: 2
        },
        mobile: {
          breakpoint: { max: 464, min: 0 },
          items: 1
        }
      };
    return(
        <Carousel
             responsive={responsive}
             autoPlay={true}   // Enables auto-slide
             autoPlaySpeed={3000} // 3 seconds per slide
             infinite={true}  // Loops the carousel
             showDots={true}  // Optional: Shows navigation dots
            
            >
          <div className='card1' >
            <img src={a} alt="" className="w-full h-auto object-cover"/>
          </div>
          <div className='card1'>
          <img src={b} alt=""className="w-full h-auto object-cover"/>
          </div>
          <div className='card1'>
          <img src={c} alt="" className="w-full h-auto object-cover"/>
          </div>
          <div className='card1'>
          <img src={d} alt=""className="w-full h-auto object-cover"/>
          </div>
        </Carousel>
    );
}