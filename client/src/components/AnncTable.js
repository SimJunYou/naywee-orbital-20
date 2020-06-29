import React from "react";
import ReactDOM from "react-dom";
import { CircularProgress, Typography } from '@material-ui/core';
import MUIDataTable from "mui-datatables";

class AnncTable extends React.Component {
  _isMounted = false; // a mounted state outside of state

  state = {
    page: 0,
    count: 1,
    data: [["Loading Data..."]],
    isLoading: false,
  };

  componentDidMount() {
    // get data for table every time the table is loaded in
    this.getData();
    this._isMounted = true;
  }

  componentWillUnmount() {
    // prevents state from updating while component is not mounted
    this._isMounted = false; 
  }

  // get data
  getData = () => {
    this.setState({ isLoading: true });
    this.getFromAPI().then(res => {
      if (this._isMounted){
        this.setState({ data: res.data, isLoading: false, count: res.total });
      }
    });
  }

  // delete data
  deleteData = (rowsDeleted) => {
    var promises = [];
    console.log(rowsDeleted);
    for (var i = 0; i < rowsDeleted.data.length; i++) {
        var indexToDelete = rowsDeleted.data[i].index;
        var idToDelete = this.state.data[indexToDelete].id;
        promises.push(fetch(`/api/students/${idToDelete}`, {
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
        fetch("/api/students")
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
          name: "s_id",
          label: "Student ID",
          options: {
            filter: true,
            sort: true,
          }
        },
        {
          name: "full_name",
          label: "Full Name",
          options: {
            filter: true,
            sort: true,
          }
        },
        {
          name: "created_at",
          label: "Timestamp",
          options: {
            filter: true,
            sort: true,
          }
        },
        {
          name: "timetable",
          label: "Timetable",
          options: {
            filter: true,
            sort: true,
          }
        },
        {
          name: "custom_reminder",
          label: "Custom Reminders",
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
        <MUIDataTable title={<Typography variant="h6">
          Announcements List
          {isLoading && <CircularProgress size={24} style={{marginLeft: 15, position: 'relative', top: 4}} />}
          </Typography>
          } data={data} columns={columns} options={options} />
      </div>
    );

  }
}

export default AnncTable;