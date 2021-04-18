<template lang="pug">
  #Home
    img(src="https://img.wallpapersafari.com/desktop/1920/1080/44/98/fpyhXL.jpg").absolute.z-2.bg.shadow-3
    .flex.flex-column.z-3.relative.main.center.items-center
      .flex.flex-row-ns.flex-column.searchbar.w-50.br4.mb5.search.pa1.shadow-3
        input(
          type="number"
          v-model="message" 
          placeholder="Search for a sol"
        ).ml2.w-90.mt2.mt0-ns.searchbar.br4.white
        button(@click="submitSearch").br4.w-20.white.dim.mr1 Search
      .flex.flex-column.center.w-50.bg-black-90.br4.shadow-3
        p.tc LATEST WEATHER ON MARS
        h1.ma0.pa0.tc Sol {{ check(weather.sol) }}
        h3.ma0.pa0.tc {{ weather.terrestrial_date.split("T")[0] }}
        .flex.justify-between.items-center.mh4
          .flex.items-center
            img(src="@/assets/sunny.png").h4.w4.ma0.pa0 
            h1.f2.ma0.pa0.ml4 {{ weather.atmo_opacity }}
          .flex.items-end
            img(src="@/assets/sunrise.png").h2.w2.pa1
            h2.mh2.pa0.mv0 {{ weather.sunrise }} - {{ weather.sunset }}
            img(src="@/assets/sunset.png").h2.w2.pa1
        .flex.flex-wrap.mh4.mt3
          .flex.flex-column.w-50
            h2.ma0.pa0 Air Temperature
            .flex.flex-column.mr4
              .flex.justify-between
                h3.ma0.pa0 Low:
                h3.ma0.pa0 {{ weather.min_temp }}°C
              .flex.justify-between
                h3.ma0.pa0 High:
                h3.ma0.pa0 {{ weather.max_temp }}°C
              hr.w-100
          .flex.flex-column.w-50
            h2.ma0.pa0 Ground Temperature
            .flex.flex-column.mr4
              .flex.justify-between
                h3.ma0.pa0 Low:
                h3.ma0.pa0 {{ weather.min_gts_temp }}°C
              .flex.justify-between
                h3.ma0.pa0 High:
                h3.ma0.pa0 {{ weather.max_gts_temp }}°C
              hr.w-100
          .flex.flex-column.w-50
            .flex.flex-column.mr4
              .flex.justify-between
                h2.ma0.pa0 Pressure:
                h3.ma0.pa0 {{ weather.pressure}} 
              hr.w-100
          .flex.flex-column.w-50.mb3
            .flex.flex-column.mr4
              .flex.justify-between
                h2.ma0.pa0 UV Index:
                h3.ma0.pa0 {{ weather.local_uv_irradiance_index}}
              hr.w-100
        .flex.flex-wrap.mb4.mh3
          div(v-for="day in filteredWeather").w-20.pa2
            .flex.flex-column.vl
              h2.ma0.pa1 Sol {{ day.sol }}
              h3.ma0.pa1 {{ day.min_temp }}°C / {{ day.max_temp }}°C
      .flex.flex-column.mt6.w-50
        h1.f2.mt0.mb4.mh0 Today's Photos
        .flex.flex-wrap
          div(v-for="photo in photos").w-33
            img(:src="photo.img_src").h5.w5.br4.shadow-3
            .flex.flex-column
              h3.white.mh0.mb0.mt2.pa0 {{ photo.rover.name }} rover
              p.third.mh0.mb0.mt2.pa0 {{ photo.camera.full_name }}
    .w-100.absolute.z-2.bg2.mt7
    .flex.justify-center.relative.z-3
      .flex.flex-column.mt7.w-70
        h1.tc.mb0 Where am I?
        .flex.justify-center.mv0
          img(src="../../mars.png").graph
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import json from "../assets/out.json"
import axios from "axios"

interface Weather {
  status: number | null
  id: number | null
  terrestrial_date: string | null
  ls: number | null
  season: string | null
  min_temp: number | null
  max_temp: number | null
  pressure: number | null
  pressure_string: string | null
  atmo_opacity: string | null
  sunrise: string | null
  sunset: string | null
  local_uv_irradiance_index: string | null
  min_gts_temp: number | null
  max_gts_temp: number | null
  sol: number
  unitOfMeasure: string | null
  TZ_Data: string | null
  abs_humidity: string | null
  wind_direction: string | null
  wind_speed: string | null
}

interface Photo {
  camera: {}
  earth_date: string
  id: number
  img_src: string
  rover: object
  sol: number
}

@Component({
  name: "Home"
})
export default class Home extends Vue {
  public photo = {
    camera: {},
    earth_date: "2021-04-06",
    rover: {},
    img_src:
      "https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03081/opgs/edr/fcam/FLB_671013737EDR_F0871958FHAZ00302M_.JPG",
    id: 821489,
    sol: 3081
  }
  public images = ""
  public photos: Photo[] = [this.photo, this.photo, this.photo]
  public filteredWeather: Weather[] = []
  public current = 1
  public message: null | number = null
  public weatherJson = {
    default: []
  }
  public weatherArr: Weather[] = []
  public weather: Weather = {
    status: 200,
    id: 2934,
    terrestrial_date: "2021-04-07T00:00:00.000Z",
    ls: 28,
    season: "Month 1",
    min_temp: -76,
    max_temp: -13,
    pressure: 850,
    pressure_string: "Higher",
    atmo_opacity: "Sunny",
    sunrise: "06:25",
    sunset: "18:17",
    local_uv_irradiance_index: "Moderate",
    min_gts_temp: -89,
    max_gts_temp: 0,
    sol: 3082,
    unitOfMeasure: "Celsius",
    TZ_Data: "America/Port_of_Spain",
    abs_humidity: null,
    wind_direction: null,
    wind_speed: null
  }
  getRandomInt(max: number): number {
    return Math.floor(Math.random() * max)
  }
  random(photos: Photo[]): Photo[] {
    if (photos.length == 1) return photos
    return [
      photos[0],
      photos[this.getRandomInt(photos.length)],
      photos[this.getRandomInt(photos.length)]
    ]
  }
  submitSearch(): void {
    var sol = 3081
    if (this.message == null) sol = 3081
    else sol = this.message
    const adjust = sol - 3081 - 6
    const searchTerm = sol - 209
    this.weather = this.weatherArr[searchTerm]
    this.filteredWeather = this.weatherArr.slice(adjust, searchTerm).reverse()
    if (this.weather.terrestrial_date == null) {
      this.fetch("2021-04-06")
    } else {
      console.log(this.weather.terrestrial_date.split("T")[0])
      this.fetch(this.weather.terrestrial_date.split("T")[0])
    }
  }
  check(value: number | string): string | number {
    return !value ? "N/A" : value
  }
  mounted(): void {
    this.weatherArr = json
    this.weatherArr.sort((a, b) => a.sol - b.sol)
    this.filteredWeather = this.weatherArr.slice(-6, this.weatherArr.length - 1).reverse()
    this.weather = this.weatherArr[this.weatherArr.length - 1]
    this.fetch("2021-04-06")
    this.getImages()
  }
  getImages(): void {
    axios.get("http://localhost:5000/fetch").then((res) => {})
  }
  fetch(date: string): void {
    axios
      .get(
        `https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=${date}&api_key=958zjnxi361gLkrtRXroHdlpVK7cNkT83bRuTEcS`
      )
      .then((response) => {
        this.photos = this.random(response.data.photos)
      })
  }
}
</script>

<style lang="scss" scoped>
.bg {
  height: 600px;
  width: 100%;
  object-fit: cover;
  filter: contrast(90%);
}
.bg2 {
  height: 1000px;
  width: 100%;
  object-fit: cover;
  background-color: #4d1518;
}
.main {
  top: 120px;
}
.search {
  height: 40px;
}
.searchbar {
  background-color: #812e33;
}
input[type="number"] {
  border: none;
  -moz-appearance: textfield;
}
input[type="number"]:focus {
  outline: none;
}
button {
  border: none;
  background-color: #4d1518;
  cursor: pointer;
}
.vl {
  border-left: 2px solid #812e33;
  border-right: 2px solid #812e33;
  height: 100%;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.graph {
  width: 800px;
  height: 800px;
}
.third {
  color: #a5a5a5;
}
</style>
