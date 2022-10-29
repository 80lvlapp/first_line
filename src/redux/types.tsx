export interface School {
    id: string
    name: string
    adress: string
  }

export interface Rating {
  sportsman: Sportsman
  place: number
  points: number
  сhangingPosition: number
}

export interface RatingSportsman {

  sportsman: Sportsman
  place: number
  points: number
  tournaments: Tournaments
}

export interface RatingTournament {

  sportsman: Sportsman
  tournament: Tournament
  points: number
  categories: Categories
}

interface Tournament {

  id: string
  name: string
  date: string
  venue: string
  type: TypeTournament

}

interface Category {

  id: string
  name: string

}

interface TypeTournament {
  id: string
  name: string
}

interface ElementTournament {

  tournament: Tournament
  points: number

}

interface ElementCategory {

  category: Category
  points: number
  place: number

}

interface Tournaments extends Array<ElementTournament>{}
interface Categories extends Array<ElementCategory>{}
  
export interface Sportsman {

  id: string
  name: string

}