<template lang="pug">
  #Home
    img(src="https://img.wallpapersafari.com/desktop/1920/1080/44/98/fpyhXL.jpg").absolute.z-2.bg
    .flex.flex-column.z-3.relative.main.center.items-center
      .flex.flex-row-ns.flex-column.searchbar.w-50.br4.mb5.search.pa1
        input(
          type="number"
          v-model="message" 
          placeholder="Search for a sol"
        ).ml2.w-90.mt2.mt0-ns.searchbar.br4.white
        button(@click="submitSearch").br4.w-20.white Search
      .flex.flex-column.center.w-50.bg-black-90.br4
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
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import json from "../assets/out.json"

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

@Component({
  name: "Home"
})
export default class Home extends Vue {
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
  submitSearch(): void {
    var sol = 3081
    if (this.message == null) sol = 3081
    else sol = this.message
    const adjust = sol - 3081 - 6
    const searchTerm = sol - 209
    this.weather = this.weatherArr[searchTerm]
    this.filteredWeather = this.weatherArr.slice(adjust, searchTerm).reverse()
  }
  check(value: number | string): string | number {
    return !value ? "N/A" : value
  }
  mounted(): void {
    this.weatherArr = json
    this.weatherArr.sort((a, b) => a.sol - b.sol)
    this.filteredWeather = this.weatherArr.slice(-6, this.weatherArr.length - 1).reverse()
    this.weather = this.weatherArr[this.weatherArr.length - 1]
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
</style>
