import { useState, useEffect } from "react";
import AlertModal from "./components/Modal";
import axios from 'axios';
import { Col, Row, Container } from "react-bootstrap";

export default function PlanValidator() {
  const [show, setShow] = useState(false);
  const [selectOptions, setSelectOptions] = useState()
  const [pbtFile, setPBTFile] = useState()
  const [pbtData, setPbtData] = useState()
  const [sbcData, setSbcData] = useState()
  const [sobData, setSobData] = useState()
  const [getType, setGetType] = useState()

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  let options = ["Primary Care Visit to Treat an Injury or Illness", "Specialist Visit", "Other Practitioner Office Visit (Nurse, Physician Assistant)",
            "Outpatient Facility Fee (e.g., Ambulatory Surgery Center)", "Outpatient Surgery Physician/Surgical Services", "Hospice Services", "Urgent Care Centers or Facilities", "Home Health Care Services", "Emergency Room Services",
            "Emergency Transportation/Ambulance", "Inpatient Hospital Services (e.g., Hospital Stay)", "Inpatient Physician and Surgical Services", "Skilled Nursing Facility", "Prenatal and Postnatal Care", "Delivery and All Inpatient Services for Maternity Care",
            "Mental/Behavioral Health Outpatient Services", "Mental/Behavioral Health Inpatient Services", "Substance Abuse Disorder Outpatient Services", "Substance Abuse Disorder Inpatient Services", "Generic Drugs", "Preferred Brand Drugs", "Non-Preferred Brand Drugs",
            "Specialty Drugs", "Outpatient Rehabilitation Services", "Habilitation Services", "Chiropractic Care", "Durable Medical Equipment", "Imaging (CT/PET Scans, MRIs)", "Preventive Care/Screening/Immunization", "Acupuncture", "Routine Eye Exam for Children", "Eye Glasses for Children",
            "Dental Check-Up for Children", "Rehabilitative Speech Therapy", "Rehabilitative Occupational and Rehabilitative Physical Therapy", "Well Baby Visits and Care", "Laboratory Outpatient and Professional Services", "X-rays and Diagnostic Imaging", "Basic Dental Care - Child", "Orthodontia - Child",
            "Major Dental Care - Child", "Abortion for Which Public Funding is Prohibited", "Transplant", "Accidental Dental", "Dialysis", "Allergy Testing", "Chemotherapy", "Radiation", "Diabetes Education", "Prosthetic Devices", "Infusion Therapy", "Treatment for Temporomandibular Joint Disorders",
            "Nutritional Counseling", "Reconstructive Surgery"]

  // let sbcScenarios = [ "Maximum Out of Pocket for Medical EHB Benefits", "Maximum Out of Pocket for Drug EHB Benefits", "Maximum Out of Pocket for Medical and Drug EHB Benefits (Total)", "Medical EHB Deductible",
  //           "Drug EHB Deductible", "Combined Medical and Drug EHB Deductible"]
  const drop = (ev) => {
    handleShow()
    ev.preventDefault()
    if (ev.dataTransfer.items) {
      // Use DataTransferItemList interface to access the file(s)
      [...ev.dataTransfer.items].forEach((item, i) => {
        // If dropped items aren't files, reject them
        if (item.kind === "file") {
          const file = item.getAsFile();
          if (file.type === "application/vnd.ms-excel.sheet.macroenabled.12") {
            // process pbt excel
            let formData = new FormData();
            formData.append("file", file);
            setPBTFile(file)
            setGetType('excel')
            getSelectOptions(formData)
          } else if (file.type === "application/pdf") {
            let formData = new FormData();
            formData.append("file", file);
            setGetType('pdf')
            getGPTResponse(formData)
          }
        }
      });
    } else {
      // Use DataTransfer interface to access the file(s)
      [...ev.dataTransfer.files].forEach((file, i) => {
        // console.log(`… file[${i}].name = ${file.name}`);
      });
    }
  }

  const allowDrop = (ev) => {
    ev.preventDefault();
  }

  const selectPlan = (e) => {
    let planData = selectOptions.find((option) => option.key === e.target.value)
    setGetType('excel')
    handleShow()
    let data = new FormData()
    data.append('plan_name', planData.key);
    data.append('sheet_name', planData.sheet);
    data.append('file', pbtFile);

    let config = {
      method: 'post',
      maxBodyLength: Infinity,
      url: `${process.env.REACT_APP_API}/pbt_data`,
      data : data
    };
    
    axios.request(config)
    .then((response) => {
      setPbtData(response.data.data)
      handleClose()
    })
    .catch((error) => {
      console.log(error);
    });
  }

  const getSelectOptions = (formData) => {
    axios.post(`${process.env.REACT_APP_API}/plan_names`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then((res) => {
      setSelectOptions(res.data)
      handleClose()
    })
  }

  const getGPTResponse = (formData) => {
    handleShow()
    axios.post(`${process.env.REACT_APP_API}/parse_pdf`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then((res) => {
      if (res.data.sbc) setSbcData(res.data.data)
      if (!res.data.sbc) setSobData(res.data.data)
      handleClose()
    })
    .catch((err) => {
      console.error(err)
      handleClose()
    })
  }

  useEffect(() => {
    if (pbtData) buildPBTable()
  }, [pbtData])

  useEffect(() => {
    if (sbcData) buildSbcTable()
  }, [sbcData])

  useEffect(() => {
    if (sobData) buildSobTable()
  }, [sobData])

  const buildPBTable = () => {
    for (let data of pbtData) {
      let inNetTr = document.getElementsByClassName(data.key)[0]
      let inNetTr2 = document.getElementsByClassName(data.key)[1]
      let oon = document.getElementsByClassName(data.key)[2]
      let inNetT1 = data.data[0].data[0].data
      let inNetT2 = data.data[0].data[1].data
      let oonD = data.data[0].data[2].data

      inNetTr.getElementsByClassName('pbt-in-network-tier-1')[0].innerHTML = inNetT1 === "nan" ? '' : inNetT1
      inNetTr2.getElementsByClassName('pbt-in-network-tier-2')[0].innerHTML = inNetT2 === "nan" ? '' : inNetT2
      oon.getElementsByClassName('pbt-oon')[0].innerHTML = oonD === "nan" ? '' : oonD
    }
  }

  const buildSbcTable = () => {
    for (let option of options) {
      let inNetTr = document.getElementsByClassName(option)[0]
      let oon = document.getElementsByClassName(option)[2]

      let sbcOptions = sbcData.filter((sbc) => sbc.key === option)

      let inNetT1 = sbcOptions[0]?.result
      let oonD = sbcOptions[1]?.result

      inNetTr.getElementsByClassName('sbc-in-network-tier-1')[0].innerHTML = inNetT1 === "nan" ? '' : inNetT1
      oon.getElementsByClassName('sbc-oon')[0].innerHTML = oonD === "nan" ? '' : oonD
    }
  }

  const buildSobTable = () => {
    for (let option of options) {
      let inNetTr = document.getElementsByClassName(option)[0]
      let oon = document.getElementsByClassName(option)[2]

      let sobOptions = sobData.filter((sob) => sob.key === option)

      let inNetT1 = sobOptions[0]?.result
      let oonD = sobOptions[1]?.result

      inNetTr.getElementsByClassName('sob-in-network-tier-1')[0].innerHTML = inNetT1 === "nan" ? '' : inNetT1
      oon.getElementsByClassName('sob-oon')[0].innerHTML = oonD === "nan" ? '' : oonD
    }
  }


  return (
    <>
    <div className="row p-2 mt-4">
      <div className="col-12">
        <div className="area">
          <div id="dropZone" onDrop={(e) => drop(e)} onDragOver={(event) => allowDrop(event)}>Drop PBT, SOB, or SBC files here one at a time</div>
        </div>
        { selectOptions &&
          <Container>
            <Row>
              <Col sm={12}>
                <div className="text-center mt-4">
                  <h4>Select a plan to continue</h4>
                </div>
              </Col>
              <Col sm={12}>
                <select className="form-select mt-1" aria-label="Default select example" onChange={(e) => selectPlan(e)}>
                <option defaultValue>Select Plan</option>
                { selectOptions.map(option => <option value={option?.key} key={option?.key}>{option?.name} - HIOS: {option?.key}</option>) }
              </select>
              </Col>
            </Row>
          </Container>
        }
        
        <table className="table table-striped table-bordered mt-4">
          <thead>
            {
              options && options.map((option, index) => {
                return (
                  <>
                    <tr key={index}>
                      <th key={index} colSpan={3} style={{backgroundColor: '#007bc4', color: '#fff'}}>
                        {option}
                      </th>
                    </tr>
                    <tr>
                      <th style={{backgroundColor: '#414141', color: '#fff'}}>PBT</th>
                      <th style={{backgroundColor: '#414141', color: '#fff'}}>SOB</th>
                      <th style={{backgroundColor: '#414141', color: '#fff'}}>SBC</th>
                    </tr>
                    <tr className={option}>
                      <td><span>In Network (Tier 1)</span><td className={`pbt-in-network-tier-1 strong`}></td></td>
                      <td><span>In Network (Tier 1)</span><td className={`sob-in-network-tier-1 strong`}></td></td>
                      <td><span>In Network (Tier 1)</span><td className={`sbc-in-network-tier-1 strong`}></td></td>
                    </tr>
                    <tr className={option}>
                      <td><span>In Network (Tier 2)</span><td className={`pbt-in-network-tier-2 strong`}></td></td>
                      <td><span>In Network (Tier 2)</span><td className={`sob-in-network-tier-2 strong`}></td></td>
                      <td><span>In Network (Tier 2)</span><td className={`sbc-in-network-tier-2 strong`}></td></td>
                    </tr>
                    <tr className={option}>
                      <td><span>Out Of Network</span><td className={`pbt-oon strong`}></td></td>
                      <td><span>Out Of Network</span><td className={`sob-oon strong`}></td></td>
                      <td><span>Out Of Network</span><td className={`sbc-oon strong`}></td></td>
                    </tr>
                  </>
                )
              })
            }
          </thead>
        </table>
      </div>
    </div>
    <AlertModal show={show} handleClose={handleClose} getType={getType} />
    </>
  )
}