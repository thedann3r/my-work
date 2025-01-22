import RiversItems from "./RiversItems"

function RiversList({rivers, setRivers}){
    return(
        <div> 
           {rivers.map(river => (
            <RiversItems
             key = {river.id}
             id = {river.id}
             name = {river.name}
             source = {river.source}
             length_in_km = {river.length_in_km}
            />
           ))}    
        </div>
    )
}

export default RiversList