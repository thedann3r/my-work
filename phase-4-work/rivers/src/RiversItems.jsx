function RiversItems({name, source, length_in_km}){
    return(
        <>
        <div>
           <h1>{name}</h1>
           <h2>{source}</h2>
           <h3>{length_in_km}</h3>      
        </div>
        </>
    )
}

export default RiversItems