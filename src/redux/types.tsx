export interface School {
    id: string
    name: string
    adress: string
  }

export interface Raiting {
  sportsman: Sportsman
  place: number
  points: number
  сhangingPosition: number
}

export interface RaitingSportsman {

  sportsman: Sportsman
  place: number
  points: number
  tournaments: Tournaments
}

interface Tournament {

  id: string
  name: string
  date: string
  venue: string

}

interface ElementTournament {

  tournament: Tournament
  points: number

}

interface Tournaments extends Array<ElementTournament>{}
  
export interface Sportsman {

  id: string
  name: string

}