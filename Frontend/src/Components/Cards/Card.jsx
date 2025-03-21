function formatCompactNumber(num) {
  return new Intl.NumberFormat("en", { notation: "compact" }).format(num);
}

function genreformatter(genre) {
  var new_genre = "";
  for (let item of genre) {
    item = item + "/";
    if (new_genre.length + item.length > 24) {
      break;
    }
    new_genre += item;
  }
  return new_genre.trim().replace(/\/$/, "");
}

export default function Card({ image_url, rating, votes, title, genre }) {
  return (
    <div>
      <div className="w-50 h-70 rounded-md ">
        <figure>
          <img className="w-50 h-70" src={image_url} alt="Movie Image" />
        </figure>
        <footer className="flex bg-black text-white ">
          <h2 className="p-1">⭐</h2>
          <h4 className="p-1 flex-1">{rating}/10</h4>
          <p className="p-1 flex-2">{formatCompactNumber(votes)}</p>
        </footer>
      </div>
      {/* <div className="text-black mt-8 w-50 bg-red-500 rounded-b-lg">
        <h1>{title}</h1>
        <p>{genreformatter(genre)}</p>
      </div> */}
      <div className="bg-grey-900 truncate overflow-hidden text-clip mt-8 rounded-b-lg w-50">
        <h1 className="pl-1">{title}</h1>
        <p className="pl-1">{genreformatter(genre)}</p>
      </div>
    </div>
  );
}
