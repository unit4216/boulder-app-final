import {useEffect, useState} from "react";
import {getMetrics, getServerHealth} from "./endpoints";
import {City} from "./App";

export const Monitoring = function ({selectedCity}:{selectedCity: City}) {
    const [healthy, setHealthy] = useState<boolean>(false)
    const [averageProcessingTime, setAverageProcessingTime] = useState<number>(0)

    useEffect(()=>{
        getMetrics()
            .then(res=>setAverageProcessingTime(res['avg_processing_time']))
        getServerHealth()
            .then(res=>setHealthy(res))
    }, [selectedCity])

    return (
        <div className='mt-4 text-lg'>
            <div>Server health: {healthy ? 'Healthy' : 'Not responding'}</div>
            <div>Average request processing time: {averageProcessingTime.toFixed(2)} ms</div>
        </div>
    )
}
