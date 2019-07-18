import {Component, OnInit} from '@angular/core';
import {HttpService} from '../services/http.service';
import {ActivatedRoute, Params} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [HttpService]
})
export class AppComponent implements OnInit {
  advertisements: any = [];
  itemsPerPage = 21;
  pagesCount = 0;
  currentPage = 1;

  district = '';
  search = '';
  priceLower = 0;
  priceUpper = 1000000;
  roomsCount = '';
  sort = 'time__desc';

  stats: any = {
    price: {
      min: 0,
      max: 1000000
    },
    rooms_count: {
      max: 10
    }
  };

  constructor(private httpService: HttpService, private activateRoute: ActivatedRoute) {
  }

  ngOnInit() {
    this.activateRoute.params.subscribe((params: Params) => {
      const page = params['page'];
      console.log(page);
    });
    this.httpService.getStats()
      .subscribe((data) => {
        this.stats = data;
        console.log(this.stats);
        this.priceLower = this.stats.price.min;
        this.priceUpper = this.stats.price.max;
      });
    this.refresh_list();
    // this.currentPage = 1;
  }

  setPage(page: number) {
    this.currentPage = page;
    this.refresh_list();
  }

  filter() {
    this.refresh_list();
  }

  refresh_list() {
    this.httpService.getAdvertisements(this.currentPage, this.itemsPerPage, this.district, this.search, this.priceLower.toString(10), this.priceUpper.toString(10), this.roomsCount, this.sort)
      .subscribe((data) => {
        // @ts-ignore
        this.advertisements = data.results;
        // @ts-ignore
        this.pagesCount = Math.ceil(data.count / this.itemsPerPage);
      });
  }
}
