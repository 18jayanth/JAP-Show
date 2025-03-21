import jap from "../../assets/jap.jpeg";
import { IoIosArrowDown } from "react-icons/io";
import { MdOutlineAccountCircle } from "react-icons/md";
import { IoSearchOutline } from "react-icons/io5";
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"></link>

export default function Home(){
    return(
    <>
    <div className="container flex justify-between pt-5" >
    <img src={jap} alt="Logo" width="1000" className="h-15 w-60"/>
<div className="search relative flex items-center border border-gray-200 rounded-md w-200 h-10 ">
        <IoSearchOutline className="search-icon text-2xl text-gray-500" /> 
        <input  type="search" placeholder="Search For Movies,Events,Plays,Sports and Activities " 
        className="w-full h-full rounded-md border-2 border-transparent outline-none text-black  "></input>
         </div>


         <span className="city text-black flex gap-10 w-20 h-20 relative ml-100  ">
            Bengaluru <span className="arrow absolute left-20 bottom-7  mb-6 pb-2"><IoIosArrowDown /></span>
             </span> 
        


        <span className="def text-black flex gap-1 relative w-50 h-10 ml-20 ">
            <span className="circle text-2xl my-auto mx-0 pb-30 pr-2 text-gray-500"><MdOutlineAccountCircle /></span> Hi, Guest 
            </span>
        </div>
   </>
    )
};
