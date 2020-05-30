import React from "react";
import ReactDOM from "react-dom";
import { CircularProgress, Typography } from '@material-ui/core';
import MUIDataTable from "mui-datatables";

class AnncTable extends React.Component {

  state = {
    page: 0,
    count: 1,
    data: [["Loading Data..."]],
    isLoading: false
  };

  componentDidMount() {
    this.getData();
  }

  // get data
  getData = () => {
    this.setState({ isLoading: true });
    this.getFromAPI().then(res => {
      console.log(res.data)
      this.setState({ data: res.data, isLoading: false, count: res.total });
    });
  }

  // FIXME: index from rowsDeleted isn't actually id
  deleteData = (rowsDeleted) => {
    var promises = [];
    console.log(rowsDeleted);
    for (var i = 0; i < rowsDeleted.data.length; i++) {
        var id = rowsDeleted.data[i].index + 1;
        promises.push(fetch(`/api/${id}`, {
                            method: "DELETE" })
                        .then(response => response.json())
        );
    }
    return Promise.all(promises)
        
  };

  // hook up with APi to get data
  getFromAPI = () => {
    return new Promise((resolve, reject) => {
        var total = 0;
        var data = {};
        
        fetch("/api")
        .then(response => response.json())
        .then(jsonData => {
            total = jsonData.length;
            data = jsonData;
        });

        setTimeout(() => {
            resolve({
              data, total
            });
          }, 2500);
    });
  }

  changePage = (page) => {
    this.setState({
      isLoading: true,
    });
    this.getFromAPI().then(res => {
      this.setState({
        isLoading: false,
        page: page,
        data: res.data,
        count: res.total,
      });
    });
  };

  render() {
    const columns = [
        {
          name: "id",
          label: "ID",
          options: {
            filter: true,
            sort: true,
          }
        },
        {
         name: "description",
         label: "Description",
         options: {
          filter: true,
          sort: true,
         }
        },
       ];

    const { data, page, count, isLoading } = this.state;

    const options = {
      filter: true,
      filterType: 'dropdown',
      responsive: 'stacked',
      serverSide: true,
      count: count,
      page: page,
      onTableChange: (action, tableState) => {
        console.log(action, tableState);
        switch (action) {
          case 'changePage':
            this.changePage(tableState.page);
            break;
        }
      },
      onRowsDelete: this.deleteData
    };
    return (
      <div>
        <MUIDataTable title={<Typography variant="title">
          Announcements List
          {isLoading && <CircularProgress size={24} style={{marginLeft: 15, position: 'relative', top: 4}} />}
          </Typography>
          } data={data} columns={columns} options={options} />
      </div>
    );

  }
}

export default AnncTable;