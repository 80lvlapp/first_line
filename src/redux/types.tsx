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
  tournaments: Tournaments
  points: number
}

interface Tournament {

  id: string
  name: string
  begin_date_tournament: string
  end_date_tournament: string
  venue: string
  type_of_tornament: TypeTournament

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

  // tournament: Tournament
  categores: Categores
  point: number
  id: string
  name: string
  begin_date_tournament: string
  end_date_tournament: string
  venue: string
  type_of_tornament: TypeTournament

}

interface ElementCategory {

  category: Category
  point: number
  place: number

}

interface Tournaments extends Array<ElementTournament>{}
interface Categores extends Array<ElementCategory>{}
  
export interface Sportsman {

  id: string
  name: string

}